# encoding: UTF-8
import shutil 
import os 
import re
import sys

rootdir = os.getcwd()
print "dir="+rootdir
filelist=[]
filelist=os.listdir(rootdir)
for i in filelist:
	j=i.replace("RIPPLE", "N-OISE")
	print j
	os.rename(i,j)

filelist=os.listdir(rootdir)
for i in filelist:
	j=i.replace("NOISE","RIPPLE")
	print j
	os.rename(i,j)

filelist=os.listdir(rootdir)
for i in filelist:
	j=i.replace("N-OISE","NOISE")
	print j
	os.rename(i,j)