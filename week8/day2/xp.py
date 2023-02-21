# ex 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age


cat1 = Cat('titi', 3)
cat2 = Cat('toto', 2)
cat3 = Cat('riri', 4.5)


def oldest_cat(cats_list):
    max_age = 0
    oldest = ''
    for cat in cats_list:
        if cat.age > max_age:
            max_age = cat.age
            oldest = cat
    return oldest


the_oldest_cat=oldest_cat([cat3,cat2,cat1])
print(f"The oldest cat is {the_oldest_cat.name}, and is {the_oldest_cat.age} years old.")

# ex 2
#Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# Create a method called bark that prints the following string “<dog_name> goes woof!”.
# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

class Dog:
    def __init__(self,name,height):
        self.name=name
        self.height=height
    def bark(self):
        print(f"{self.name} goes woof!")
    def jump(self):
        print(f"{self.name} jumps {self.height*2} cm high!")

davids_dog=Dog("Rex",50)
print(davids_dog.name,davids_dog.height)
davids_dog.jump()
davids_dog.bark()

sarahs_dog=Dog("Teacup",20)
print(sarahs_dog.name,sarahs_dog.height)
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height>sarahs_dog.height:
    print(f"{davids_dog.name} is bigger")
else:
    print(f"{sarahs_dog.name} is bigger")

#ex 3
class Song:
    def __init__(self,lyrics):
        self.lyrics=lyrics
    def sing_me_a_song(self):
        for song in self.lyrics:
            print(song)


stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()


# ex 4
class Zoo:
    def __init__(self,zoo_name):
        self.animals=[]
        self.name=zoo_name
    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
    def get_animals(self):
        for animal in self.animals:
            print(animal)
    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    # def sort_animals(self):
    #     sorted(self.animals)
