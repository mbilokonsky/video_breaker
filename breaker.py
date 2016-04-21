from sklearn.cluster import MiniBatchKMeans
import numpy as np
import argparse
import cv2
import pandas as pd

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--image", required=True, help="Path to the image.")
    parser.add_argument("-c", "--clusters", required=True, type=int, help="# of clusters.")
    args = vars(parser.parse_args())

    image_vector = get_image_as_vector(args["image"])
    clusters = get_clusters(image_vector)

    print(clusters)


def get_clusters(image_vector, cluster_count=16):
    clt = MiniBatchKMeans(n_clusters=cluster_count)

    labels = clt.fit_predict(image_vector)

    rgb_centers = get_rgb_centers(clt);
    cluster_freqs = get_cluster_freqs(labels);

    cluster_df = pd.DataFrame(rgb_centers, columns=['r', 'g', 'b'])
    cluster_df['frequency'] = cluster_freqs.values()
    return cluster_df.sort_values('frequency', ascending=False)

def get_rgb_centers(clt):
    cluster_centers = clt.cluster_centers_.astype("uint8").reshape(16, 1, 3)
    centers = cv2.cvtColor(cluster_centers, cv2.COLOR_LAB2BGR)
    return np.hstack([centers[:, :, i] for i in (2, 1, 0)])

def get_cluster_freqs(labels):
    label_list = labels.tolist();
    label_df = pd.DataFrame(label_list, columns=['cluster'])
    label_df['value'] = np.ones(len(label_list))
    return label_df.groupby('cluster').count()['value'].map(lambda v: v / float(label_df.value.sum())).to_dict()

def get_image_as_vector(image_path):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    image = image.reshape((image.shape[0] * image.shape[1], 3))
    return image


if __name__ == '__main__':
    main()
