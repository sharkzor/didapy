import random
computer_number = random.randint(1,5)
keuze = 0
tries = 3
while keuze != computer_number and tries > 0:
    print("Guess the number between 1 and 5 you have " + str(tries) + " left")
    keuze = int(input())
    if keuze not in range(0,6) :
        print("Waarde ligt niet tussen 1 en 5")
        continue
    
    if keuze == computer_number:
        print("gefeliciteerd het was idd " + str(keuze)) 
        exit()
    elif keuze > computer_number:
        print("Kies een lager nummer")
    elif keuze < computer_number:
        print("Kies een hoger nummer")
    else:
        print("helaas niet goed. probeer opnieuw " + str(computer_number))
    tries-=1

print("Helaas. uw kansen zijn op \nHet getal was " + str(computer_number))