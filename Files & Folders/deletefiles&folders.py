import shutil
import os

# shutil.rmtree('/home/ayush/Music/Final')

os.chdir('/home/ayush/Downloads')

for filename in os.listdir() :
    if filename.endswith('.png') :
        print(filename)
# for deleteing files os.unlink(filename)