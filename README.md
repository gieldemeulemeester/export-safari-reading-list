[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://raw.githubusercontent.com/manbearwiz/youtube-dl-server/master/LICENSE)

# export-safari-reading-list

Export Safari reading list to webloc files.

The Python script requires a `-i` or `--ifile` argument with the path to Safari's bookmarks plist file. Optionally, you can add a `-o` or `--opath` argument with the path to the output directory for the .webloc files. If ommitted, the output will go to the current working directory.

Safari's `Bookmarks.plist` can be found in `~/Library/Safari/Bookmarks.plist`. However, this location is by default no longer accessible with Terminal in macOS Mojave (10.14) or later. You can either copy this file somewhere accessible or [grant full disk access to Terminal](https://appletoolbox.com/seeing-error-operation-not-permitted-in-macos-mojave/).

Usage example:
```shell
python3 export_safari_reading_list.py -i ~/Desktop/Bookmarks.plist -o ~/Desktop/rlist
```
