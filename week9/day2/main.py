
# def exercise1():
#     """ Printing the results of three built in functions: int abs input."""
#     print(int('5'))
#     print(abs(-55))
#     print(input('enter something:'))
#
# print(exercise1.__doc__)
# exercise1()

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    #Your code starts HERE
    def __str__(self):
        return f'{self.amount} {self.currency}s'


    def __int__(self):
        return self.amount

    def __repr__(self):
        return f'{self.amount} {self.currency}s'

    def __add__(self, other):
        if type(other) == (int or float):
            return self.amount + other
        if type(other) == Currency:
            if self.currency != other.currency:
                raise TypeError(f' Cannot add between Currency type {self.currency} and {other.currency}')
            else:
                return self.amount+other.amount

    def __iadd__(self, other):
        if type(other) == (int or float):
            self.amount += other
            return self
        if type(other) == Currency:
            if self.currency != other.currency:
                raise TypeError(f' Cannot add between Currency type {self.currency} and {other.currency}')
            else:
                self.amount += other.amount
                return self



c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1),int(c1),repr(c1),c1+5,c1+c2,c1)
c1 += 5
print(c1)
c1 += c2
print(c1)


