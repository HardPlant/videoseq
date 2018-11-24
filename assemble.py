import sys
import os
from optparse import OptionParser
def main():
    
    parser = OptionParser()
    parser.add_option("-v", "--invert", action="store_const", const="--invert", dest="invert", default="")
    parser.add_option("-r", "--reverse", action="store_const", const="--reverse", dest="reverse", default="")
    parser.add_option("-b", "--backtoback", action="store_const", const="--backtoback", dest="backtoback", default="")

    parser.add_option("--intype", dest="intype", default="png")
    parser.add_option("--outtype", dest="outtype", default="png")
    

    parser.add_option("--in", dest="inpath", default="extract")
    parser.add_option("--out", dest="outpath", default="result/out.png")
    parser.add_option("-s", "--start", type=int, dest="start")
    parser.add_option("-e", "--end", type=int, dest="end")
    parser.add_option("-f", "--frame", type=int, default=30, dest="frame")
    '''
    parser.add_option("-l", "--rotateleft", type=int, default=270, dest="angle")
    parser.add_option("-r", "--rotateright", type=int, default=90, dest="angle")
    '''

    (options, args) = parser.parse_args()

    if options.start == None or options.end == None:
        exit()

    start = options.start
    end = options.end
    frame = options.frame
    
    inverted = options.invert
    revert = options.reverse
    backtoback = options.backtoback

    intype = options.intype
    outtype = options.outtype

    print(options)

    count = end-start-1
    if backtoback:
        count = count * 2

    os.system("del /Q resized\*.*")
    print("python resize_and_copy.py -s {} -e {} {} {} {} --intype {} --outtype {}".format(start, end, inverted, revert, backtoback, intype, outtype))
    os.system("python resize_and_copy.py -s {} -e {} {} {} {} --intype {} --outtype {}"\
        .format(start, end, inverted, revert, backtoback, intype, outtype))
    if options.outtype == "png":
        print("python make_apng.py {}".format(frame))
        os.system("python make_apng.py {}".format(frame))
    elif options.outtype == "gif":
        print("python make_gif.py {} {}".format(count, frame))
        os.system("python make_gif.py {} {}".format(count, frame))

if __name__ == "__main__":
    print('[*]assemble.py : lets make png or gif!')
    main()