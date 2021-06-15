import random

computer_number = random.randint(1,5)
#print("Dit is "  + str(computer_number))
keuze = 0
computer_number = 1
while keuze != computer_number:
    computer_number = random.randint(1,5)
    print("Guess the number between 1 and 5")
    keuze = int(input())
    if keuze not in range(0,6) :
        print("Waarde ligt niet tussen 1 en 5")
        quit()


    if (keuze == computer_number) : 
        print("gefeliciteerd het was idd " + str(keuze)) 

    else:
        print("helaas het nummer was " + str(computer_number))
