import codecs
import os
from glob import glob

try:
    if not os.path.exists('Fixed'):
        os.makedirs('Fixed')
except:
    print("couldn't create directory")
    quit()
for filename in glob('*.srt'):
    BLOCKSIZE = 1048576
    with codecs.open(filename, 'r', "Windows-1256") as sourceFile:
        with codecs.open("fixed/"+filename, "w", "utf-8") as targetFile:
            while True:
                contents = sourceFile.read(BLOCKSIZE)
                if not contents:
                    break
                targetFile.write(contents)
