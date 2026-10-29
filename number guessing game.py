import random 

secret = random.randint (1,256)
guess = int(input("Enter your Guess : "))

while guess != secret:
  
  if guess < secret:
    print ("Low")
  else:
    print ("High")
  guess = int(input("Enter your Guess : "))

print (" Nice, the number was : ",secret)