words={}
times=int(input("How many words do you want to enter: "))
for i in range(times):
    word=input("Enter the word: ")
    count=words.get(word,0)
    words[word]=count+1
print(words)
