while True: 
    print("1. Analyse a New text ", "2. Exit ")
    answer=int(input("Enter your choice: "))
    if(answer==2):
        break
    if(answer==1):
        sen=input("Enter a sentence: ")
        if(sen[0].islower()):
            print(sen.capitalize())
        else:
            pass
        
        print("The length of the sentence is ", len(sen))
        specific=input("Enter the word you want to count: ")
        i=0
        count=0
        while i<len(sen):
            if sen[i].lower() in "aeiou":
                print("letter", i+1, "is vowel")
            if sen[i]==specific:
                count+=1
            i+=1

        print("The word's count is ", count)
        if(sen.endswith(".")):
            print("The sentence ends with a period.")
        elif(sen.endswith("?")):
            print("The sentence ends with a question mark.")
        elif(sen.endswith("!")):
            print("The sentence ends with a exclamation mark.")
        else:
            print("The sentence has unknown puncuation mark.")

        question=input("Do you want to replace any word? ")
        if(question.lower()=="yes" or question.lower()=="y"):
            specify=input("Enter the word you want to replace: ")
            specify_new=input("Enter the word to be replaced with: ")
            print(sen.replace(specify, specify_new))
        elif(question.lower()=="no" or question.lower()=="n"):
            pass 
            
        print("The starting five characters are: ", sen[0:5])
        print("The ending 5 characters are: ", sen[-5:])
