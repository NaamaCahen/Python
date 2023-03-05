import operators

print(operators.add_operator(5,2))
print(operators.divide_operator(8,2))

from operators import add_operator,divide_operator
print(add_operator(57,25))
print(divide_operator(7854785458,8))
from operators import add_operator as add,divide_operator as divide
print(add(55,11))
print(divide(55,11))
