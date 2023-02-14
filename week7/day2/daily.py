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
str_matrix=''
last='a'
for column in columns:
    for char in column:
        if not last.isalpha() and not char.isalpha():
            str_matrix+=' '
            last='a'
        elif char.isalpha():
            str_matrix += char
            last=char
        else:
            last=char
print(str_matrix)
