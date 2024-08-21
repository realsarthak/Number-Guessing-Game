import random
computer=random.randrange(1,10)
user=int(input("Enter the number :\n"))

if user>computer:
    print("computer:",computer)
    print("Your guessed Number is too High")

elif computer>user:
    print("Computer number:",computer)
    print("Your Guessed Number is too low")
else:
    print("Computer Number:",computer)
    print("Your Guessed Number is Equal ! You win!!")