import os

fileType = 'mp3'
numberOfFiles = 100
outputDir = 'C:\Users\Zhelun Gai\desktop'

# create directory
def createDirectory(output_dir):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

# create a file in specified directory
def createFile(file_type, output_dir):
    with open(os.path.join(output_dir, filename), 'w') as dummyFile:
        dummyFile.write(os.urandom((1024)))

# generate non-repeat file name
def generateFileName():
    return 'dummy_file_%s.%s'%