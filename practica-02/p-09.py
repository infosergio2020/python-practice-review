# Observar el programa GUESS THE NUMBER en la página web, modifíquelo para que el rango
# del número a adivinar sea de 1 hasta 50 y que corte su ejecución cuando lo adivine. Agregar
# además que luego de 3 intentos mostrar la pista, una única vez, si el número es par o impar.

# font:  https://inventwithpython.com/invent4thed/chapter3.html

# This is a Guess the Number game.
import random
guessesTaken = 0
print('Hello! What is your name?')
myName = input()
# number = random.randint(1, 20)
number = random.randint(1, 50)
print('Well, ' + myName + ', I am thinking of a number between 1 and 50.')

for guessesTaken in range(6):
    print('Take a guess.') # Four spaces in front of "print"
    guess = input()
    guess = int(guess)
    if guess < number:
        print('Your guess is too low.') # Eight spaces in front of "print"
    if guess > number:
        print('Your guess is too high.')
    if guessesTaken == 2:
        if number % 2 == 0:
            print('The number I was thinking is pair')
        else:
            print('The number I was thinking is impair')
    if guess == number:
        break
if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Good job, ' + myName + '! You guessed my number in ' +
          guessesTaken + ' guesses!')
if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')