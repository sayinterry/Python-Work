import os
import time
import datetime
import sys
import shutil

movedir = r"E:\Songs"
basedir = r"C:\Users\Chodizzle\Desktop\osu!\Songs"
lastRun = datetime.datetime(2014, 2, 7, 0, 0)
timeFromLastRun = time.mktime(lastRun.utctimetuple())

for root, dirs, files in os.walk(basedir):
    for filename in files:
        if filename.endswith(".mp3") or filename.endswith(".ogg"):
            fullpath = os.path.join(root, filename)
            if (os.path.getmtime(root) >= timeFromLastRun):
                size = os.path.getsize(fullpath)
                if size > 800000:
                    base, extension = os.path.splitext(fullpath)
                    new_filename = os.path.split(os.path.dirname(fullpath))[1] + extension
                    shutil.copyfile(fullpath, os.path.join(movedir, new_filename))
print("done")
