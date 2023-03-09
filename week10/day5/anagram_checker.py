class AnagramChecker:
    def __init__(self):
        with open('./sowpods.txt','r') as f:
            self.file=f.read()

    def is_valid_word(self,word):
        return word.upper() in self.file

    def get_anagrams(self,word1):
        words_list=self.file.split('\n')
        anagrams=[]
        for word2 in words_list:
            if self.is_anagram(word1.upper(),word2):
                anagrams.append(word2)
        return anagrams
    def is_anagram(self,word1,word2):
        return ''.join(sorted([*word1])) == ''.join(sorted([*word2]))
    def print_file(self):
        print(self.file)

ac=AnagramChecker()

print(ac.is_valid_word('aa'))
print(ac.get_anagrams('meat'))
