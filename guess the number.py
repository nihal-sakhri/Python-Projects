import random

n = random.randint(1, 10)
count = 1
guess_chances = 3
name= input("Hi, let's play a game. But first what's your name?")
print("Hello", (name) , "I am NIHAL, the developper of this guessing game, I am going to guess a number between 1 and 10, you need to guess it")
print("Remember, you only have 3 chances to guess right")
while 1 <= guess_chances:
    num = int(input("Guess the Number: "))
    if num > n:
        print("Your guess was too high: Guess a number lower than", num)
    elif num < n:
        print("Your guess was too low: Guess a number higher than", num)
    else:
        print("You Win!")
        print(count, "gueses you took")
        break
    guess_chances -= 1
    print(guess_chances, "Guesses Left")
    count += 1
    print()

print("Game over")
print("Number is ", n)

# follow @code_snail on Instagram