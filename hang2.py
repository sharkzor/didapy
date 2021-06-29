import random

# constants
HANGMAN = (
"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")
MAX_WRONG  = len(HANGMAN) 
WORDS = ("powershell","python","animal","didacticum")
wrong = 0
#word = random.choice(WORDS)
word ="pow"
your_guess = len(word) * "_"



#Modify your code in such a way to show the correct gueses on the _ _ _.
#So if the word was 'pope' and you guessed 'o' the program should still say
#you got ot right but then show _ o _ _.
#The program should then ask for a guess again and show _ o _ _ .
# If you then guess 'p' it should tell you again you guessed it correctly and should display
# p o p _
# With wrong guesses it should show the correct HANGMAN picture.
# Furthermore the while loop should break if the correct word was guessed. So now you have 2 conditions when the loop
#could break. The MAX in the tuple HANGMAN or the correct word was guessed.
#DIFFICULT ! So good luck
print("welcome to Hangman \n ")


geradenletters=""
while MAX_WRONG > wrong and word != your_guess:
    print("This is the word sofar in " + your_guess + " try guess a letter\n")

    
    print( " Take a guess")
    guess = input()
    if guess in geradenletters:
        print("De letter " + guess+ " heb je al gebruikt")
    else:
        geradenletters+=guess
        if guess in word:
            print( "Yes " + guess +  " is in the word \n \n")
            new = ""
            for i in range (len(word)):
                if guess == word[i]:
                    new+=guess
                else:
                    new+= your_guess[i]
            your_guess= new
        
            

        else:
            print("Sorry " + guess + " is not in the word\n")
            print(HANGMAN[wrong])
            wrong+=1
        
if your_guess == word:
    print("\n Yes geraden")
else:
    print("\n pogingen op sukkel")
     