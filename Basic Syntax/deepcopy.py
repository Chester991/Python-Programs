import copy

spam = [1,2,3,4,5,6]
cheese = spam
cheese[1] = 7
print(cheese)
print(spam)
print('\n')
spam1 = [1,2,3,4,5,6]
cheese1 = copy.deepcopy(spam)
cheese1[1]=7
print(spam1)
print(cheese1)