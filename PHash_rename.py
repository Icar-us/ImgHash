
#imports
import os
import sys
from difflib import SequenceMatcher
from PIL import Image
import imagehash

#defs
def similar(a, b):
     print ( SequenceMatcher(None, a, b).ratio() )

path = '/home/solar45/Pictures/MEGAsync/Edits/'   #define PATH to dir to be checked



for filename in os.listdir(path):   #run through PATH and get names
    print(filename)
    hash = imagehash.average_hash(Image.open(path+filename))    #Hash files in PATH to be able to compare them
    print(hash)    


    src = path+filename
    dst = path+str(hash)

    os.rename(src, dst)
pass

