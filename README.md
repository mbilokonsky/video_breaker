So, put a video into the `videos/` folder, let's call it "foo.mp4".

To generate frames from your video, run:
  `./break.sh foo.mp4`

Once you have your frames, you can use the python breaker script to extract color data from a given frame:
  `python breaker.py -i "output/foo.mp4/frame_000064.png" -c 16`

This will run, spit out a bunch of python warnings that I can't suppress, and then print out the top 16 colors in that frame. I'm not 100% sure that these are correct - still have some work to do explore this space - but they were at some point correct, before I transferred them out of iPython and into this script, and I'm confident that they can be again if they're not!

Note that this python script:
  1. is running against a single frame, that you pass in as an argument.
  2. doesn't write anything out to a file - it just prints its output.
  3. is not exactly lightning fast.

So we've got some work to do, but this seems to more or less do what we want.
