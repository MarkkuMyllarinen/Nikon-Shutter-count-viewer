NIKON Shutter count viewer
=

**Tested and works with Nikon D3300**

This shows how many images has been taken on your camera

# What do I need?

**Note:** All commands are in Linux Ubuntu. See Python for Windows


1. You need the Python 3
2. You need to install `exifread` with `pip3 install exifread`
3. Image in `.NEF` format


# Example output

    python3 shutter.py DSC_0085.NEF

    Camera Model:  NIKON D3300
    Total shutter counts:  7323


# How to use 

### Run with command
    python3 shutter.py image_file.NEF

replace image_file.NEF with your own RAW imagefile from camera.