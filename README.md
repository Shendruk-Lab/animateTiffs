# animateTiffs
## A script to efficiently make videos from TIFs

Python scripts that read in TIF files and create videos. It makes videos of any TIF files with the usergiven prefix and suffix of the TIF file names. 

## Requirements
 - Requires [ffmpeg](https://ffmpeg.org/)

## Overview 
The `animateTiffs.py` script takes in a path as a **required** argument and makes animations out of every TIF within all subsequent directories. Optional arguments make the script more versatile.

Arguments:
- `-h`, Help (list of arguments). 
- `path`, Location of the parent directory that includes all TIFs.
- `--prefix`, `-p` Start of file name
- `--leadingZeros`, ``-z` Number of leading zeros 
- `--suffix`, ``-s` End of file name
- `--videoFormat`, `-v` Different video formats
- `--framerate`, `-r` Frames per second

## Usage
Command line example:
```
python animateTiffs.py ~/Documents/research/results/tiff2avi/ -p img_channel000_position000_time -z 9 -s _z000.TIF -v avi -r 10
```

Taking advantage of the defaults, this is the same as:
```
python animateTiffs.py ~/Documents/research/results/tiff2avi/
```
