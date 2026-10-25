import os
import glob
import re
import shutil

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)', text) ]

files = [f for f in glob.glob("*.txt")]

#ff = files.sort(key=lambda f: int(filter(str.isdigit, f)))
#print(ff)

for ff in sorted(files, key=natural_keys):
    title = 'titles/{}_title.txt'.format(ff.split('.')[0])
    #tt = ff.split('.')[0]
    #title = f"{tt}_title.txt"
    print(title)
    shutil.copyfile(ff, title)


