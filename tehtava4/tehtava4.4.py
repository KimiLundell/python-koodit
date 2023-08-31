import random
luku = random.randint(1,10)
arvaus = int(input("Arvaa luku väliltä 1-10: "))
while luku!=arvaus:
    if arvaus>luku:
        print("Liian suuri arvaus")
    elif arvaus<luku:
        print("Liian pieni arvaus")
    arvaus = int(input("Arvaa luku väliltä 1-10: "))

print("Oikein")