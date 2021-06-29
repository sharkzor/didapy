names = ["bla","flap","flop"]

print (range(len(names)))

guess = input()
for i in range(len(names)):
    if guess == names[i]:
        print("gevind")



word = "hangman"

guess = input()

for i in range(len(word)):
    if guess == word[i]:
        print("found something")