import random

guess_made =0
name = input("what is you name ")

number = random.randint(1, 20)
print("well " + name + " i am thinking of a number between 1 and 20 ")
while guess_made < 10:
    guess = int(input("take  a guess : "))
    guess_made += 1
    if guess > 20:
        print(" please guess number in between 1 and 20")
    elif guess < number:
        print("you guess is too low ")
    elif guess > number:
        print("your guess is to high ")
    elif guess == number:
        break

if(guess== number):
    print("congrats " + name + " you guess the number in " + str(guess_made) + " guesses")
else:
    print("nope the number i was thinking is " + str(number))