from anagram_checker import AnagramChecker

finish = False
while not finish:
    users_input = input('please type a single word (alphabetical characters only) or exit (q) :')
    if users_input == 'q':
        finish = True
    else:
        users_input = users_input.strip()
        for letter in users_input:
            if not letter.isalpha():
                print('your word cannot contain white-spaces or unalphabetical characters')
                break
        an_ch=AnagramChecker()
        anagrams=an_ch.get_anagrams(users_input)
        print(f"""Your Word: {users_input}
        this is a valid English word
        Anagrams for your word: {anagrams}""")



