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



#Modify your code in such a way to show if you won or lost at the termination of the while loop!

print("welcome to Hangman \n ")



while MAX_WRONG > wrong and word != your_guess:
    print("This is the word sofar in " + your_guess + " try guess a letter\n")

    
    print( " Take a guess")
    guess = input()
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