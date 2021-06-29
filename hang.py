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
word = random.choice(WORDS)
print(word)
your_guess = len(word) * "_"

print("Take A guess " + your_guess) 

loops=0
guess = ""
geraden = ""
while loops < MAX_WRONG:
    guess = input()
    if guess in word:
        print("Yes " + guess + " is " + str(word.count(guess)) +" times in the word")
        geraden = geraden + guess
    else:
        print("No  " + guess + " is not in the word")
    loops = loops + 1

for i in range(len(woord)):
    print(woord[i])


#print(your_guess)


#Write code that will continue to ask you to guess a letter
#If a letter is in the word the program should tell you this
#The program should terminate when the maximum tries has been reached.
#Don't worry about displaying the HANGMAN drawings or even the letters guessed, just show that the
#letter is found and don't go beyond the max elements in the HANGMAN Tuple

