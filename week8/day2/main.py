# Old MacDonald’s Farm


class Farm:
    def __init__(self,farm_name):
        self.farm_name=farm_name
        self.animals = {}

    def add_animal(self, animal_name: str, num: int = 1):
        self.animals[animal_name] = num
    def get_info(self):
        return (f"""
        {self.farm_name}'s Farm
            {for animal in self.animals:
                
            }
        """)


macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
