import random
number = random.randint (1,10)
player_name  = input("hello, what's your name?")
number_of_guesses = 0
print ("I'm glad to meet you", player_name, "let's play a game, I will think of a number between 1 and 10 and you will guess it, alright? don't forget, you only have 3 chances!:")
while number_of_guesses < 3:
  number_of_guesses += 1
  guess = int(input("guess!"))
if guess < number :
   print ("your estimation is too low, go up a little" )
if guess > number :
 print ("your estimation is too high, go down a bit")
if guess == number :
   print("congratulations" , player_name , ", you guessed the number in" , number_of_guesses, "tries!" )
else:
 print ("close but not cigar, you couldn't guess the number, it was", number,) 