import array as arr
a = arr.array('i',[45,50,55,88,96,5])
y = a[1:5]
print(y)
for i in y :
    print(i,end=' ')
print('\n')
z = a[4:]
for i in z :
    print(i,end=' ')
print('\n')