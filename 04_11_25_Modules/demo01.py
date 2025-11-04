import random # for generating any random stuff

random_number = random.randint(1, 10)

user_input = int(input("Enter a number: "))

while user_input != random_number:
  print("You guessed Wrong! Try Again!")

  user_input =  int(input("Enter a number: "))

print(f"You guessed right! The number was: {random_number}")