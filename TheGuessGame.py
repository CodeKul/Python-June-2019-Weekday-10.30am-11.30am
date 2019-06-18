import random

while True:
    n1 = random.randint(1,10)
    n2 = int(input("Enter a number: "))
    if n2 == 0:
        break
    if n1 == n2:
        print("Winner Winner Chicken Dinner")
    else:
        print("Better luck next time")