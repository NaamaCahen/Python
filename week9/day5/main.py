class Human:
    def __init__(self, id_number: str, name: str, age: int, priority: bool, blood_type: str):
        self.id_number = id_number
        self.name = name
        self.age = age
        self.priority = priority
        if blood_type in ['A', 'B', 'AB', 'O']:
            self.blood_type = blood_type
        self.family = []

    def __eq__(self, other):
        if isinstance(other,Human):
            if self.age == other.age:
                return True
            return False

    def __lt__(self, other):
        if isinstance(other,Human):
            if self.age < other.age:
                return True
            return False


    def add_family_member(self, person):
        self.family.append(person)
        person.family.append(self)


class Queue:
    def __init__(self):
        self.humans = []

    def __str__(self):
        str=[]
        for person in  self.humans:
            str.append(person.name)
        return ','.join(str)

    def add_person(self, person):
        if person.priority or person.age > 60:
            self.humans.insert(0, person)
        else:
            self.humans.append(person)

    def find_in_queue(self, person):
        return self.humans.index(person)

    def swap(self, person1, person2):
        index_person1 = self.humans.index(person1)
        self.humans[index_person1] = person2

    def get_next(self):
        if len(self.humans) == 0:
            return None
        return self.humans.pop(0)

    def get_next_blood_type(self, blood_type):
        if len(self.humans) == 0:
            return None
        person = next(person for person in self.humans if person.blood_type == blood_type)
        self.humans.remove(person)
        return person

    def sort_by_age(self):
        priorities = []
        others = []
        saved_index=0
        for person in self.humans:
            if person.priority:
                    priorities.append(person)
            else:
                    others.append(person)

        self.humans = sorted(priorities,reverse=True) + sorted(others,reverse=True)
        return self.humans

    def rearange_queue(self):
        for i, person in enumerate(self.humans):
            if i < len(self.humans)-1:
                if self.humans[i + 1] in person.family:
                    j = i + 1
                    while self.humans[j] in person.family:
                        j += 1
                    save_change = self.humans[j]
                    self.humans[j] = self.humans[i + 1]
                    self.humans[i + 1] = save_change


naama = Human('222', 'naama', 19, False, 'A')
mother = Human('225', 'mother', 39, False, 'AB')
father = Human('111', 'father', 55, True, 'A')
yoyo = Human('444', 'yoyo', 12, False, 'O')
teddy = Human('22244', 'teddy', 74, True, 'B')
nono = Human('2281', 'nono', 21, True, 'A')
naama.add_family_member(mother)
naama.add_family_member(father)
queue1=Queue()
queue1.add_person(naama)
queue1.add_person(mother)
queue1.add_person(father)
queue1.add_person(yoyo)
queue1.add_person(teddy)
queue1.add_person(nono)

print(queue1.find_in_queue(teddy))


print(queue1)

queue1.get_next()


queue1.get_next_blood_type('A')

queue1.sort_by_age()
print(queue1)

queue1.rearange_queue()

print(queue1)
