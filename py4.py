import random
computer_number = random.randint(1,5)
keuze = 0
tries = 3
gebruikt = []

while keuze != computer_number and tries > 0:
    print("Guess the number between 1 and 5 you have " + str(tries) + " left")
    keuze = int(input())
    if keuze not in range(0,6) :
        print("Waarde ligt niet tussen 1 en 5")
        continue
    
    while keuze in gebruikt:
        print("Je heb dit al een keer geraden. Kies wat anders")
        keuze = int(input())
        
        
    gebruikt.append(keuze) 
    

    if keuze == computer_number:
        print("gefeliciteerd het was idd " + str(keuze)) 
        exit()
    
    
    elif keuze > computer_number:
        print("Helaas niet goed. Kies een lager nummer")
    elif keuze < computer_number:
        print("Helaas niet goed. Kies een hoger nummer")
    tries-=1

print("Helaas. uw kansen zijn op \nHet getal was " + str(computer_number))

#test