
import sys
import os
import imutils
import cv2
from optparse import OptionParser

inverted = False
size = (400,225)
startnum = 0
rotate_angle = 90 # 270

def extract_image(idx, count, intype, outtype, rotate):
    global size
    image = cv2.imread("extract/frame{:04d}.{}".format(idx, intype))
    if rotate:
            image = imutils.rotate_bound(image, rotate_angle)
    print("[*]Resize_and_copy.py : extract frame{:04d}.{}".format(idx, intype), end='\r')
    resized_image = cv2.resize(image, size)
    cv2.imwrite("resized/frame{:04d}.{}".format(count, outtype), resized_image, [cv2.IMWRITE_PNG_COMPRESSION,9])

def main(start, end, inverted=False, revert=False, backtoback=False, intype="png", outtype="png"):
    global size
    count = startnum

    if inverted:
        import imutils
        size = tuple(reversed(size))
        

    if not revert:
        for idx in range(start, end):
            extract_image(idx,count, intype, outtype, inverted)
            count = count + 1
            
    else:
        for idx in range(end,start,-1):
            extract_image(idx,count, intype, outtype, inverted)

            count = count + 1

    if backtoback:
        for idx in range(end,start,-1):
            extract_image(idx,count, intype, outtype, inverted)

            count = count + 1
        
if __name__ == "__main__":
    
    parser = OptionParser()
    parser.add_option("-s", "--start", type=int, dest="start")
    parser.add_option("-e", "--end", type=int, dest="end")

    parser.add_option("-i", "--intype", dest="intype", default="png")
    parser.add_option("-o", "--outtype", dest="outtype", default="png")
    '''
    parser.add_option("-v", "--invert", type=int, dest="inverse", default=0)
    parser.add_option("-r", "--reverse", type=int, dest="reverse", default=0)
    parser.add_option("-b", "--backtoback", type=int, dest="backtoback", default=0)
    '''
    parser.add_option("-v", "--invert", action="store_true", dest="isInverse", default=False)
    parser.add_option("-r", "--reverse", action="store_true", dest="isReverse", default=False)
    parser.add_option("-b", "--backtoback", action="store_true", dest="isBacktoback", default=False)

    (options, args) = parser.parse_args()

    if options.start == None or options.end == None:
        exit()
    print('[*]Resize_and_copy.py : argv is : {}'.format(sys.argv))
    outtype = options.outtype
    if options.outtype == "gif":
        outtype = "jpg"
    
    directory = 'resized'
    if not os.path.exists(directory):
        os.makedirs(directory)

    print('[*]Resize_and_copy.py : running')
    main(options.start, options.end + 1,\
    inverted=options.isInverse, revert=options.isReverse, backtoback=options.isBacktoback,\
    intype=options.intype, outtype=outtype)
    print('')
    if outtype == 'png':
        print("[*]PNGQuant is running")
        os.system("pngquant --force --quality 0-10 resized/*.png --ext .png")