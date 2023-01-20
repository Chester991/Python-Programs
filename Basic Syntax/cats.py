numofcats = input()
try:
    if int(numofcats) >= 4:
        print('That is a lot!')
    else:
        print('Nice !')
except ValueError:
    print('You did not enter a number')
