# ex 1
import random


def display_message():
    print("I am learning python")


display_message()

# exercise 2
def favorite_book(title):
    print(f"one of my favorite books is {title}")
favorite_book(title="sefer Devarim")

#exercise 3
def describe_city(city,country='Israel'):
    print(f"{city} is in {country}")
describe_city('bnei brak')

#exercise 4
def compare_random_with_num(num):
    random_num=random.randint(1,100)
    if(random_num==num):
        print("wow!! these are exactly the same numbers!")
    else:
        print(f"oops, the numbers {num} and {random_num} are not the same... \n retry your chance...")
compare_random_with_num(5)

#exercise 5
def make_shirt(size="L",text_to_print="I love Python"):
    print(f"The size of the shirt is {size} and the text is: {text_to_print}")

make_shirt()
make_shirt("M")
make_shirt("XS","I hate Python")
make_shirt(size='xl',text_to_print='wooow i`m using keyword arguments!!')

#exercise 6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians(magician_list):
    for magician_name in magician_list:
        print(magician_name)
def make_great(magician_list):
    for i in range(len(magician_list)):
        magician_list[i]='the great '+magician_list[i]

show_magicians(magician_names)
make_great(magician_names)
show_magicians(magician_names)
