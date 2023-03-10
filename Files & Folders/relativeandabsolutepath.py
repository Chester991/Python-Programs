import os

print(os.getcwd())
print(os.path.abspath('spam.png'))
print(os.path.abspath('../../spam.png'))
print('\n')
print(os.path.isabs('..\\..\\spam.png'))
print(os.path.isabs('/Downloads/Books'))

print(os.path.relpath('/folder1/folder2/spam.png', '//folder1'))
print('\n')
print(os.path.dirname('/folder1/folder2/spam.png'))
print(os.path.basename('/folder1/folder2/spam.png'))
print (os.path.basename('/folder1/folder2'))    