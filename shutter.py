#!/usr/bin/env python
import sys
from exifread import process_file


def usage():
    print("""
    Usage:
        Please enter the raw file name.
    """)
    exit(1)
                
def main():
    if len(sys.argv) != 2:
        usage()

    rawfile = sys.argv[1]
    exif_decode(rawfile)

def exif_decode(rawfile):
    with open(rawfile, "rb") as ifh:
        tags = process_file(ifh)
        try:
            print("Camera Model: ", tags['Image Model'])
            print("Total shutter counts: ", tags['MakerNote TotalShutterReleases']) 
        except KeyError:
            print("No EXIF data found.")

if __name__ == "__main__":
    main()
