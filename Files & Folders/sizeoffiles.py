import os

totalsize = 0
for filename in os.listdir('/home/ayush/Documents/Books') : #iterate over all the files and directories
    if not os.path.isfile(os.path.join('/home/ayush/Documents/Books',filename)) : #if the current iteration is not a file(is a directory or a folder) skip it
        continue
    totalsize = totalsize + os.path.getsize(os.path.join('/home/ayush/Documents/Books',filename))
print(str(totalsize) + ' kb')
mb = round(totalsize / 1024, 2)
print(str(mb) + ' mb')