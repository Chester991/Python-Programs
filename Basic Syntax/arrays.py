import array as arr
a = arr.array('i', [1, 2, 3])
for i in range(0, 3):
    print(a[i])
print('\n')
b = arr.array('d', [4.5, 7.2, 8.8])
for i in range(0, 3):
    print(b[i])
print('\n')
b.reverse()
for i in range(0, 3):
    print(b[i])         