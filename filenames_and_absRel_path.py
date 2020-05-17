#Absolute filepaths always begin with the root folder
#Relative filepaths does not
import os

print(os.path.join('folder1', 'folder2', 'folder3', 'folder4'))

direct = r'C:\Users\Runej\Desktop\Memes'
totalSize = 0
for filename in os.listdir(direct):
    if not os.path.isfile(os.path.join(os.path.join(direct, filename))):
            continue
    totalSize = totalSize + os.path.getsize(os.path.join(os.path.join(direct, filename)))
print(totalSize)
