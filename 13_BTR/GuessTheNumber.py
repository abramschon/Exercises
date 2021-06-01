# Have the user try to guess the secret number

secret_no = 3301
guess = int(input("Guess a number:\n"))  # catch not integer error if feeling fancy
no_guess = 1

while not(guess==secret_no):
    if guess < secret_no:
        print("Got anything higher?")
    else:
        print("Got anything lower?")
    guess = int(input("Guess a new number:\n"))
    no_guess += 1 

print(f"You tried {no_guess} times")