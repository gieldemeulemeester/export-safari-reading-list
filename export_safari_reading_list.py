#!/usr/local/bin/python3

import sys, os, argparse, plistlib, webloc

def write_weblocs(plistDict, args):
    childCount = 0
    if 'Children' in plistDict.keys():
        for child in plistDict['Children']:
            childCount += write_weblocs(child, args)
    if 'ReadingList' in plistDict.keys():
        filename = f"{plistDict['URIDictionary']['title'].replace('/', '-')}.webloc"
        webloc.write(f"{args.opath}/{filename}", plistDict['URLString'])
        childCount += 1
        if args.verbose: print(filename)
    return childCount

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export Safari reading list to webloc files.")
    parser.add_argument("-i", "--ifile", type=str, required=True, dest="rlistFile", help="path to reading list plist file")
    parser.add_argument("-o", "--opath", type=str, dest="opath", help="output directory")
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    args = parser.parse_args()

    rlist = plistlib.readPlist(args.rlistFile)

    if args.opath == None:
        args.opath = os.getcwd()
    elif not os.path.isdir(args.opath):
        os.mkdir(args.opath)    
    args.opath.rstrip('/')
    
    print("{} weblocs created".format(write_weblocs(rlist, args)))