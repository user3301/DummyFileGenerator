import os
import random
import string
import time
from random import randint

fileType = 'mp3'
numberOfFiles = 100
outputDir = r'C:\Users\zhelun\Desktop\aa'

# create directory
def createDirectory(output_dir):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

# create a file in specified directory
def createFile(output_dir):
    with open(os.path.join(output_dir, generateFileName()), 'w') as dummyFile:
        dummyFile.write(''.join(random.sample(string.ascii_letters + string.digits, random.randint(20, 40))))

# generate non-repeat file name
def generateFileName():
    localtime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    return 'dummy_file_%(filename)s.%(filetype)s'%{"filename": localtime, "filetype": fileType}