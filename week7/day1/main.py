# Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it
# . And also it must return both addition and subtraction in a single return call
def calculate(num1,num2):
    add=num1+num2
    sub=num1-num2
    return add,sub

add_calc,sub_calc=calculate(88,55)
print(add_calc,sub_calc)