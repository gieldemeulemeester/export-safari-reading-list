#!/usr/local/bin/python3

import sys, os, argparse, plistlib, webloc

def get_bookmarks_dict(bookmarksFile: str) -> dict:
    if bookmarksFile == None:
        if sys.stdin.isatty():
            print("the following arguments are required: -i/--ifile")
            exit(1)
        return plistlib.loads(sys.stdin.buffer.read())
    
    try:
        with open(bookmarksFile, 'rb') as f:
            return plistlib.load(f)
    except FileNotFoundError:
        print(f"the bookmarks file '{bookmarksFile}' was not found")
        exit(1)
    except PermissionError:
        print(f"the bookmarks file '{bookmarksFile}' is not accessible")
        exit(1)

def sanitize_output_dir(path: str) -> str:
    if path == None:
        path = os.getcwd()
    elif not os.path.isdir(path):
        os.mkdir(path)
    return path.rstrip('/')

def write_weblocs(bookmarksDict: dict, args) -> int:
    childCount = 0
    if 'Children' in bookmarksDict.keys():
        for child in bookmarksDict['Children']:
            childCount += write_weblocs(child, args)
    if 'ReadingList' in bookmarksDict.keys():
        filename = f"{bookmarksDict['URIDictionary']['title'].replace('/', '-')}.webloc"
        webloc.write(f"{args.opath}/{filename}", bookmarksDict['URLString'])
        childCount += 1
        if args.verbose: print(filename)
    return childCount

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export Safari reading list to webloc files.")
    parser.add_argument("-i", "--ifile", type=str, dest="bookmarks", help="path to Safari's bookmarks file")
    parser.add_argument("-o", "--opath", type=str, dest="opath", help="output directory")
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
    args = parser.parse_args()

    bookmarksDict = get_bookmarks_dict(args.bookmarks)
    args.opath = sanitize_output_dir(args.opath)
    count = write_weblocs(bookmarksDict, args)
    print(f"{count} weblocs exported")
