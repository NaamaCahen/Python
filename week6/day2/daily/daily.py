
word=input("please insert a ten letters word:")
if len(word)!=10:
    if len(word)>10:
        print("string too long")
    else:
        print("string not long enough")
else:
    print(word[0],word[len(word)-1])
    x=''
    for i in word:
        x+=i
        print(x)
print(random.shuffle(word))
