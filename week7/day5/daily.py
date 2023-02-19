# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
def sort_sequence(string):
    splitted_list=string.split(',')
    sorted_list=sorted(splitted_list)
    sorted_string=','.join(sorted_list)
    return sorted_string


print(sort_sequence('without,hello,bag,world'))


def shorter_way(string):
    return ','.join(sorted(string.split(',')))


print(shorter_way('without,hello,bag,world'))