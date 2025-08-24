import random

random_number = random.randint(1, 50)

print(" Welmcome to the number guessing game")
print("Guess a number between 1 and 50")

attempt = 0

while True:
  guess = int(input("Enter your guess: "))
  attempt += 1
  if guess < random_number:
    print("Too low!")
    print("Try again")
    print("Attempts: ", attempt)
  elif guess > random_number:
    print("Too high!")
    print("Try again")
    print("Attempts: ", attempt)
  else:
    print("Congratulations! You guessed the number in", attempt, "attempts.")
