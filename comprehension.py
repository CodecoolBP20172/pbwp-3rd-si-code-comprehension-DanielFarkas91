import random #importing random module from python libary

guessesTaken = 0 #guessesTaken variable assigned to 0

print('Hello! What is your name?') #console output: ...
myName = input() #variable myName is assigned to user input

number = random.randint(1, 20) #variable number is assigned to a random number generated within 1-20 (including 1 and 20).
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') # console output: Well,...

while guessesTaken < 6: #Function While is going to run until guessesTaken variable is less then six
    print('Take a guess.') #console output: ...
    guess = input() #guess variable assigned to user input
    guess = int(guess) #guess variable is converted to integer

    guessesTaken += 1 #add 1 to guessesTaken variable until while function runs.

    if guess < number: # if guess variable is less than number variable
        print('Your guess is too low.') #console output: ...

    if guess > number: # if guess variable is bigger than number variable
        print('Your guess is too high.') #console output: ...

    if guess == number: # if guess variable equals with number variable
        break #the function terminates.

if guess == number: # if guess variable equals number variable
    guessesTaken = str(guessesTaken) # guessesTaken variable converted to a string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!') #console output: ...

if guess != number: # if guess variable is not equal with number variable
    number = str(number) #number variable is converted to a string
    print('Nope. The number I was thinking of was ' + number) #console output: ...
