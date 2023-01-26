import array as arr

a = arr.array('i', [])
n = int(input("Enter the length of the array "))

for i in range(n):
    x = int(input("Enter the next value "))
    a.append(x)

for i in a:
    print(i, end=' ')

m = int(input("Enter the value for which index is to be found "))
for i in range(0, n):
    if a[i] == m:
        print("Index is : " + str(i))
        break
