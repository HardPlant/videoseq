import sys
import cv2
import imutils
import numpy as np
import subprocess
import os

filetype = "png"
rotate = False
rotate_angle = 270 # 90

def do_cv(filename):
    vidcap = cv2.VideoCapture(filename)
    success,image = vidcap.read()
    if not success:
        print(success)
    count = 0
    
    size = (400,225)

    while success:
        success,image = vidcap.read()
        image = cv2.resize(image, size)
        if rotate:
            image = imutils.rotate_bound(image, rotate_angle)

        cv2.imwrite("extract/frame{}.{}".format(count,filetype), image, [cv2.IMWRITE_PNG_COMPRESSION, 9 ])
        if cv2.waitKey(10) == 27:
            break
        count += 1
    
def do_ffmpeg(filename):
    subprocess.call(["ffmpeg","-i",filename, "extract/frame%04d.png",\
    "-compression_level","100", "-r","30"])# "-ss","00:00:20.0"

if __name__ == "__main__":
    print('[*]extract.py : extract from a movie!')
    
    directory = 'extract'
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    if len(sys.argv) == 1:
        filename = "out.mp4"    
    else:
        filename = sys.argv[1]

    if len(sys.argv) > 2 and sys.argv[2] == "--opencv":
        do_cv(filename)
    else:
        do_ffmpeg(filename)