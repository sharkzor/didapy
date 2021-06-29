import random

woord = random.choice(("dorothe","wonderland","mad","hatter"))
print(woord)

voegsel = len(woord) * '_'


print("here is your word " + voegsel + " take a guess") 

inputstring = ""
while inputstring != woord:
    inputstring = input()
    if inputstring == woord:
        print("YEAH you guessed it, it was " + woord)
    else:
        print("NOOO sorry guess again")    
    
