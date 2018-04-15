import os

fileType = 'mp3'
numberOfFiles = 100
outputDir = 'C:\Users\Zhelun Gai\desktop'

# create directory
def createDirectory(self, output_dir):
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

# create a file in specified directory
def createFile(self, file_type, output_dir):
