import random
def game():
    b=input()
    d=random.randint(1, 20)
    print(f"Well, {b}, I am thinking of a number between 1 and 20.\nTake a guess.")
    c=int(input())
    i=1
    while c!=d:
        if c<d:
            print("Your guess is too low.\nTake a guess.")
        else:
            print("Your guess is too high.\nTake a guess.")
        i+=1
        c=int(input())
    print(f"Good job, {b}! You guessed my number in {i} guesses!")
print("Hello! What is your name?")
game()