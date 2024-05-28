"""
	Script animates tiffs into videos using ffmpeg
"""

import argparse
import os
from subprocess import call

###########################################################
### User arguments
###########################################################
parser = argparse.ArgumentParser(description='Script to convert TIFFs to video.')
parser.add_argument("path", type=str, help="Location of the parent directory that includes all TIFs.",default="./")
parser.add_argument("-p", "--prefix", type=str,help="Start of file name",default="img_channel000_position000_time")
parser.add_argument("-z", "--leadingZeros", type=int,help="Number of leading zeros in file name",default=9)
parser.add_argument("-s", "--suffix", type=str,help="End of file names",default="_z000.tiff")
parser.add_argument("-v", "--videoFormat", type=str,help="Different video formats",default="avi")
parser.add_argument("-r", "--framerate", type=int,help="Framerate",default=10)
args = parser.parse_args()
print("Arguments:")
for arg, value in vars(args).items():
	print(f"\t{arg}: {value}")
path=args.path
prefix=args.prefix
leadingZeros=args.leadingZeros
suffix=args.suffix
format=args.videoFormat
framerate=args.framerate

###########################################################
### Initialization
###########################################################
if(path[-1]!='/'):
	path=path+'/'
if not os.path.isdir(path):
	print("The directory %s does not exist."%(path))
	os.mkdir(path)
if(format[0]!='.'):
	format='.'+format
suffixWithoutFormat=suffix
if suffix.endswith(".tiff"):
	tiffFormat=".tiff"
	suffixWithoutFormat=suffix.replace(tiffFormat,'')
elif suffix.endswith(".TIFF"):
	tiffFormat=".TIFF"
	suffixWithoutFormat=suffix.replace(tiffFormat,'')
elif suffix.endswith(".tif"):
	tiffFormat=".tif"
	suffixWithoutFormat=suffix.replace(tiffFormat,'')
elif suffix.endswith(".TIF"):
	tiffFormat=".TIF"
	suffixWithoutFormat=suffix.replace(tiffFormat,'')
else:
	print("No file format given. Assuming '.TIF'")
	tiffFormat=".TIF"
	suffix=suffix+tiffFormat

###########################################################
### Find directories
###########################################################
allDirs = [f[0] for f in os.walk(path)]
hasTiffs = [0] * len(allDirs)
for d in range(len(allDirs)):
	for f in os.listdir(allDirs[d]):
		if f.lower().endswith(tiffFormat):
			hasTiffs[d]=1
dirs=[]
for d in range(len(allDirs)):
	if(hasTiffs[d]): 
		dirs.append(allDirs[d])
		if(dirs[-1][-1]!='/'):
			dirs[-1]=dirs[-1]+'/'

###########################################################
### Animate
###########################################################
aniName=prefix+suffixWithoutFormat+format
for d in dirs:
	name='%s%s'%(d,aniName)
	if os.path.isfile(name):
		call("rm %s"%name,shell=True)
	myCommand = "ffmpeg -framerate "+str(framerate)+" -i %s%s"%(d,prefix)+"%0"+str(leadingZeros)+"d%s "%(suffix)+name
	call(myCommand,shell=True)

###########################################################
### Done
###########################################################
exit()
