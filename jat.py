MAX_WRONG  = len(HANGMAN) 
WORDS = ("powershell","python","animal","didacticum")
wrong = 0
word = random.choice(WORDS)
#word ="pow"
your_guess = len(word) * "_"
print(your_guess)
guess = input("Raad een letter: ")
#Write code that will continue to ask you to guess a letter
#If a letter is in the word the program should tell you this
#The program should terminate when the maximum tries has been reached.
#Don't worry about displaying the HANGMAN drawings or even the letters guessed, just show that the
#letter is found and don't go beyond the max elements in the HANGMAN Tuple
while wrong <= MAX_WRONG and guess != word :
    for i in range(len(word)):
        if guess in word[i]:
            print("The letter ", guess, " is in the word!")
        else :
            print("too bad, the letter ", guess, " is not in the word. Try again!")
            wrong+=1
    guess = input("Raad een letter: ")