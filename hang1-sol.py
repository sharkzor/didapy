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

print(your_guess)


#you already have some code. 

#Write code that will continue to ask you to guess a letter 

#If a letter is in the variable word the program should tell you this 

#The program should terminate when the maximum tries has been reached.(in this case the maximum in the tuple HANGMAN) 

#Show the HANGMAN drawings in progressing order every time a wrong guess has been done. 

#At the end the when the max guesses (max in tuple HANGMAN) the final drawing should be displayed. 

#In theory this program could go on forever if you keep guessing a correct letter. 


print("welcome to Hangman \n \n")
print(word)
geraden = ""
compleet = ""
while MAX_WRONG > wrong and word != compleet:
    compleet = ""
    print( " Take a guess")
    guess = input()
    if guess in word:

        for i in range (len(word)):
            if guess == word[i]:
                print( "Yes " + guess +  " is in the word \n \n")
                geraden+=guess
                for i in range(len(word)):
                    if word[i] in geraden:
                        print(word[i], end = '')
                        compleet+=word[i]
                    else:
                        print("_", end = '')
                        compleet = compleet + "_"
                    

    else:
        print("Sorry " + guess + " is not in the word\n")
        print(HANGMAN[wrong])
        wrong+=1
        for i in range(len(word)):
            if word[i] in geraden:
                print(word[i], end = '')
            else:
                print("_", end = '')
        
if geraden == word:
    print("\n Yes geraden")
else:
    print("\n pogingen op sukkel")
     
