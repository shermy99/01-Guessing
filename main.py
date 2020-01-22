import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


quit = False
range = 100

while not quit:
    random_number = random.randint(1,range)
    count = 1
    number = -1
    while number != random_number:
        number = input("Please guess a number between 1 and {}: ".format(range))
        if not number.isdigit():
            print("Please only use numbers!")
        else:
            number = int(number)
            count = count + 1
            print("Sorry, you didn't guess the correct number")
            if number > random_number:
                print("that number was too high.")
            elif number < random_number:
                print("that number was too low.")
    print("Good job! You guessed the right number!")
    print("You guessed it in {} attempts.".format(count))
    play_again = input("\nDo you want to play again (yes or no)? ")
    play_again = play_again.lower()
    if play_again == "yes" or play_again == "y":
        quit = False
    else:
        quit = True

print("\n\nThank you for playing! Come back soon!")