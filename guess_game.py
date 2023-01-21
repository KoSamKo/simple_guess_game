# guess game

counter = 0  #while loop
secret_number = 6
guess_limit = 5

print("Range of numbers ís form 0 to 9")
print(f"Guess limit is {guess_limit}")

while counter < guess_limit:
    guess = int(input("Guess number: "))
    counter += 1
    if guess > 9:
        print("You are out of range")
    elif guess == secret_number:
        print("Bingo!")
        break
else:
    print("You failed!")