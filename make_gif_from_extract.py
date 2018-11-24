import sys
import subprocess
def main(start, end, outfile="out.gif"):
    subprocess.call(["magick",\
    "-size","225*400",\
    "-delay","1x30",\
    "extract/frame%d.jpg[{}-{}]".format(start,end),\
    'result/{}'.format(outfile)])
    
if __name__ == "__main__":
    if len(sys.argv) < 3:
        start=int(sys.argv[1])
        end=int(sys.argv[2])
    if len(sys.argv) < 4:
        outfile=sys.argv[3]
        print('[*]make_gif_from_extract : jpg to gif converter!')
        main(start,end, outfile)