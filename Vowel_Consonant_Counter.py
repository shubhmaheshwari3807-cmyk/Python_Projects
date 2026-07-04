def count_letter(word):
    count_vowel=0
    count_conso=0
    i=0
    while i<len(word):
        print(word[i])
        if(word[i]=='a' or word[i]=='e' or word[i]=='i' or word[i]=='o' or word[i]=='u'):
            print("It's a vowel")
            count_vowel+=1
        else:
            print("It's a conso")
            count_conso+=1
        i+=1
    print("Vowel: ", count_vowel)
    print("Conso: ", count_conso)
    return (count_vowel, count_conso)

word=input("Enter the word: ")
count_letter(word)