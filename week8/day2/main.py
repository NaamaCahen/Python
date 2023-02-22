# Old MacDonald’s Farm


class Farm:
    def __init__(self,farm_name):
        self.farm_name=farm_name
        self.animals = {}

    def add_animal(self, animal_name: str, num: int = 1):
        if animal_name in self.animals.keys():
            self.animals[animal_name] += num
        else:
            self.animals[animal_name] = num
    def get_info(self):
        return (f"""
        {self.farm_name}'s Farm
        
        {self.animals}
        
            I-E-I-E-0!
        """)
    def get_animal_types(self):
        return list(self.animals.keys())
    def get_short_info(self):
        types=self.get_animal_types()
        return (f"{self.farm_name}'s farm has {types}")


macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())

# add a method called get_animal_types to the Farm class.
# This method should return a sorted list of all the animal types (names) in the farm.
# With the example above, the list should be: ['cow', 'goat', 'sheep'].

# Add another method to the Farm class called get_short_info.
# This method should return the following string: “McDonald’s farm has cows, goats and sheep.”.
# The method should call the get_animal_types function to get a list of the animals.