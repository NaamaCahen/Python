word = input("please insert a word:")
dict_word={}
i=0
for letter in word:
     if letter in dict_word:
        dict_word[letter].append(i)
     else:
         dict_word[letter]=[i]
     i+=1
print(dict_word)