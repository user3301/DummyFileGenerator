# DummyFileGenerator

[![license](https://img.shields.io/github/license/slashsBin/styleguide-git-commit-message.svg)](https://github.com/user3301/DummyFileGenerator/blob/master/LICENSE)<br/>
DummyFileGenerator generates dummy files with arbitrary file size for testing purpose.
## Environment
* Python 3.5 or above

## Usage Example
###Basic Usage
This program affords user to generate dummy files with random size under a specified directory.<br/>
Modify the `config.ini`file to specify:
```
[DEFAULT]
fileType = *TYPE OF FILE YOU WANT TO GENERATE* (eg: mp3, wav, txt etc.)
numberOfFiles = *HOW MANY FILES WANTED* (eg: 10, 500, 100000(WARNNING: large quantity may takes long time to run))
outputDir = *OUTPUT DIRECTORY* (create new directory if not exist)
```

After the configuration is done, run the `program.py` in the terminal of interest:
```
$ python program.py
```

### Tweak Your Output Size
As the dummy files are for testing purpose, the generated file size are no more than 1KB, if you expect large size file, simply modify the `createFile()` method under `./lib/core.py`:

```
ef createFile():
    for i in range(numberOfFiles):
        with open(os.path.join(outputDir, generateFileName()), 'w+') as dummyFile:
            dummyFile.write(''.join(random.sample(string.ascii_letters + string.digits, random.randint(20, 40))))
```
## Contributing
* clone this repo to your local (`git clone https://github.com/user3301/ssml-builder.git`)
* Create your own branch (`git checkout -b my-new-branch`)
* Commit changes (`git commit -am ":sparkles:my feature"`)
* Push (`git push origin my-new-branch`)
* Pull request

## Author
* User3301
:e-mail: base64 c3Rhbl9nYWlASG90bWFpbC5jb20=