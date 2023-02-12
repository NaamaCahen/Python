word = input("please insert a word:")
dic_word={
    "d":[5]
}
for i, letter in enumerate(word):
     if dic_word[letter] in dic_word:
        dic_word[letter].insert(i)
     else:dic_word[letter]=[i]
print(dic_word)