words=[]
times=int(input("How many words do you want to enter: "))
for i in range(0, times):
    word=input("Enter the word: ")
    words.append(word)
word_set=set(words)
print("You have entered", len(words), "words")
print("You have entered", len(word_set), "unique words")
print(word_set)
