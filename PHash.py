
#imports
import os
import sys
from difflib import SequenceMatcher
from PIL import Image
import imagehash

#defs
def similar(a, b):
     print ( SequenceMatcher(None, a, b).ratio() )

#path = '/home/solar45/Documents/Github/ImgHash/pics/'   #define PATH to dir to be checked

path = '/home/solar45/Documents/Github/ImgHash/pics/'

l = []

for filename in os.listdir(path):   #run through PATH and get names
    print(filename)
    hash = imagehash.average_hash(Image.open(path+filename))    #Hash files in PATH to be able to compare them
    l.append(hash)
pass



img1 = str(l[0])
img2 = str(l[1])
similar(img1,img2)
