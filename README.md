[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://raw.githubusercontent.com/manbearwiz/youtube-dl-server/master/LICENSE)

# export-safari-reading-list

Export Safari's reading list to webloc files.

The Python script requires a `-i`/`--ifile` argument with the path to Safari's bookmarks file or a byte stream from `stdin`. Optionally, you can add a `-o`/`--opath` argument with the path to the output directory for the .webloc files. If omitted, the .webloc files will be written to the current working directory.

Safari's `Bookmarks.plist` file can be found in `~/Library/Safari/`. However, this directory is by default no longer accessible with Terminal in macOS Mojave (10.14) or later. You can either copy this file somewhere accessible or [grant full disk access to Terminal](https://appletoolbox.com/seeing-error-operation-not-permitted-in-macos-mojave/).

Usage examples:
```shell
python3 export_safari_reading_list.py -i ~/Desktop/Bookmarks.plist -o ~/Desktop/rlist
```
```shell
cat ~/Desktop/Bookmarks.plist | export_safari_reading_list.py -o ~/Desktop/rlist
```
