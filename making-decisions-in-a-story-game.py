print ("welcome to my first game!")
print (" I am Nihal SAKHRI, the developer of this game")
print("let's have some fun together!")
name = input("what is your name? ")
age = int(input ("what is your age?"))

print("Hello", name, "you are", age, "years old") 

health = 10

print ("you are starting with", health, "health")
if age >=18 : 
  print ("you are old eough to play!")
elif age >= 14 : 
  print ("you can play with supervision")
else: 
  print ("you are not old enough to play!")
  
wants_to_play = input ("do you want to play? ").lower()
if wants_to_play == "yes" :
    print ("Let's play!")
    left_or_right = input (" First choice; you are lost in the woods and you find 2 different ways, where do you go? (left/right)? ")
if left_or_right == "right":
    ans = input("Oh no! moving sand pulls you down!")
else : 
 left_or_right == "left"
print ("Good job!")

accross_or_around= input("Nice, you follow the path and reach a lake. Do you swim across or go around (accross/around)?")
if accross_or_around == "around":
       print ("you went around and reached the other side of the lake")
else:
        accross_or_around == "accross"
        print ("you managed to get accross, but were bit by a fish and lost 5 health")
        health -=5
        print ("-5 health")
     

ans = input("you notice a house and a river, which do you go to (house/river)?")
if ans == "house":
      print("you go to the house and are greted by the owner... he doesn't like you and lost 5 health")
      health -= 5
else:
  print("you swim accross the river successfully!")

if health <= 0:
        print("you now have 0 health and you lose the game..")
        print ("I hope you enjoyed the game, play it again to discover the other options!")
else:
        print(" you have survived, you win!")
        print ("I hope you enjoyed the game, play it again to discover other options!")


      



    

    


