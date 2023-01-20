import random
print('Hey ! What is your name?')
name = input()
print('Hey! ' + name + ' I am thinking of a number between 1 and 20')
secretnumber = random.randint(1, 20)

for guesstaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretnumber:
        print('Your guess is too low')
    elif guess > secretnumber:
        print('Your guess is too high')
    elif guess == secretnumber:
        break

if guess == secretnumber:
    print('Correct! You guessed the number in ' + str(guesstaken) + ' guesses')
else:
    print('Nope wrong number number of chances exceeded I was thinking of' + str(secretnumber))
