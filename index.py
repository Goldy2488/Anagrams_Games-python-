import random
f=open("Anagrams_Games.txt","r")
a=f.readlines()
index=random.choice(range(len(a)-1))
words=a[index].split(',')
# print(words)
# words=["apple","mango","banana","pineapple","chery",'January','February','March','April','MayJune','July','August','September','October','November','Decembery']
print("~"*44)
print("~~~~~~~~~ Welcome in Anagrams Game ~~~~~~~~~")
print("~"*44) 
game=input("You want to play the game enter 'y' : ").lower()
while game=="y": 
    chances=int(input("Enter how many Chances are you want for win the Game : "))
    word=random.choice(words)
    word=word.lower()
    jumble="".join(random.sample(word,len(word)))
    while chances:
        print("The word is",jumble)
        guess=input("enter the correct speling: ").lower()
        if guess == word:
            print("Correcct Guess!!")
            print("YOU WON 🥇!!!")
            print()
            game=input("You want to play again enter 'y'otherwise enter 'n': ").lower()
            if game=="n":
                break
            else:
                game="y"
            break
        else:
            chances-=1
            print("Incorrect Guess 😲!!")
            print("Remaning chances are:",chances)
            print()

    else:
        print("all you chances are exhausted.")
        print("YOU LOSE 👎")
        print("correct answar is",word)
        print("")
        game=input("Whether you want to play again?(y/n) : ").lower()
        if game!="y":
            break
print("🥰🥰 Thank you for playing 🥰🥰.")


