# solve the matrix
a = ["7", "i", "3"]
b = ['T', 's', 'i']
c = ['h', '%', 'x']
d = ['i', '', '#']
e = ['s', 'M', '']
f = ['$', 'a', '']
g = ['#', 't', '%']
h = ['^', 'r', '!']

columns = zip(a, b, c, d, e, f, g, h)
# print(list(columns))
str_matrix=[]
last='a'
for column in columns:
    for char in column:
        if char.isalpha():
            str_matrix.append(char)
            last = char
        elif not last.isalpha() :
            str_matrix.append(' ')
            last = 'a'
        else:
            last=char
print(''.join(str_matrix))