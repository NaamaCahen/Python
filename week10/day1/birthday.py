import datetime

my_birthday = datetime.datetime(2023, 5, 7)
now = datetime.datetime.now()
days_remaining = my_birthday - now
print('my birthday is in ' + str(days_remaining))
