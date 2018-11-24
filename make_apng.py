import os
import sys
'''
import cv2
from apng import APNG, FrameControl


start, end = (3665, 3753)
width, height = (400, 225)
fc = FrameControl(width=width, height=height, delay=10, delay_den=10)
im = APNG()
#files = tuple(("extract/frame{}.png".format(idx), 1) for idx in range(5054, 5164,3))
files = tuple(("resized/frame{}.png".format(idx), 0) for idx in range(start, end))

for file, delay in files:
    im.append(file, width=width, height=height, delay=1, delay_den=60000)
im.save("result/result.png")
'''
def main(fps):
    directory = 'result'
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    result = "result/output.png"
    sequence = "resized/frame0000.png"
    startnum = 1
    print("[*]make_apng.py : running with result : {}, squence : {}, fps:{}".format(result, sequence, fps))\
        
    os.system("apngasm.exe {} {} {} {}".format(result, sequence, 1, fps))

if __name__ == "__main__":
    if len(sys.argv) == 2:
        main(int(sys.argv[1]))
    else:
        main(30)