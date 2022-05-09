#!/usr/bin/env python
import subprocess
import os
from multiprocessing import Pool
src = "/home/student-02-06d3243ead76/data/prod/"
dest = "/home/student-02-06d3243ead76/data/prod_backup/"


files = os.listdir(src)
def walkFolder(f):
    for root,dirs,fil in os.walk(src+f):

        if dirs:
            for directory in dirs:
               # print("")
                subprocess.call(["rsync","-arq",os.path.join(src,f,directory),os.path.join(dest,f)])
        else:
            subprocess.call(["rsync","-arq",os.path.join(src,f),os.path.join(dest,f)])


        for fi in fil:
            path = root[root.find(f):]
            subprocess.call(["rsync","-arq",os.path.join(src,path,fi),os.path.join(dest,path)])

if __name__ == "__main__":
    pool=Pool(len(files))
    pool.map(walkFolder,files)
#subprocess.call(["rsync", "-arq", src, dest])

