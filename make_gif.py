import sys
import subprocess
def main(count, frame=20, outfile="out.gif"):
    subprocess.call(["magick",\
    "-size","225*400",\
    "-delay","1x{}".format(frame),\
    "resized/frame%d.jpg[0-{}]".format(count),\
    'result/{}'.format(outfile)])
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit(0)
    print(sys.argv)
    count = int(sys.argv[1])
    frame = int(sys.argv[2])
    print('[*]make_gif.py : lets make gif!')
    main(count, frame=frame)
    
    