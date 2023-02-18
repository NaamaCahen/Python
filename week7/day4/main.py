def try_to_divide_by_zero():
    try:
        5 / 0
    except ZeroDivisionError:
        print("you cannot divide by zero!!")

try_to_divide_by_zero()
