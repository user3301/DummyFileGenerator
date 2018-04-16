import os
import random
import string
import time
import configparser
from threading import Thread

config = configparser.ConfigParser()
config.read('config.ini')

fileType = config['DEFAULT']['fileType']
outputDir = config['DEFAULT']['outputDir']
numberOfFiles = config.getint('DEFAULT', 'numberOfFiles')


# create directory
def createDirectory(output_dir):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)


# create a file in specified directory
def createFile():
    for i in range(numberOfFiles):
        with open(os.path.join(outputDir, generateFileName()), 'w+') as dummyFile:
            dummyFile.write(''.join(random.sample(string.ascii_letters + string.digits, random.randint(20, 40))))
            dummyFile.close()
            time.sleep(3)

# generate non-repeat file name
def generateFileName():
    localtime = time.strftime("%Y%m%d%H%M%S", time.localtime())
    return 'dummy_file_%(filename)s.%(filetype)s' % {"filename": localtime, "filetype": fileType}
