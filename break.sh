rm -rf output/$1
mkdir output/$1
mkdir output/$1/data
ffmpeg -i videos/$1 -r 24 output/$1/frame_%06d.png
