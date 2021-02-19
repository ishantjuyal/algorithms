import random

n = int(input("Enter any number between 1 and 100: "))

low = 1
high = 99

while True:
    guess = random.randint(low, high)
    print("Guess is:", guess)
    if guess == n:
        print("Game Completed")
        break
    else:
        print("Press U if the number is higher and L if the number is lower")
        sign = input().lower()
        if sign == 'u':
            low = guess
        elif sign == 'l':
            high = guess
        else:
            print("Invalid input")