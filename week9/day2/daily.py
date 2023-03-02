class Circle:
    def __init__(self, radius=0, diameter=0):
        if radius == 0:
            self.diameter = diameter
            self.radius = diameter / 2
        elif diameter == 0:
            self.radius = radius
            self.diameter = radius * 2

    def circle_area(self):
        return 3.14 * self.radius ** 2

    def __str__(self):
        return f"this circle has a radius of {self.radius} cm, and a diameter of {self.diameter} cm"

    def __add__(self, other):
        if type(other) == Circle:
            return self.radius + other.radius

    def __gt__(self, other):
        if type(other) == Circle:
            if self.radius > other.radius:
                return True
            return False

    def __lt__(self, other):
        if type(other) == Circle:
            if self.radius < other.radius:
                return True
            return False

    def __le__(self, other):
        if type(other) == Circle:
            if self.radius <= other.radius:
                return True
            return False

    def __eq__(self, other):
        if type(other) == Circle:
            if self.radius == other.radius:
                return True
            return False

    def __ne__(self, other):
        if type(other) == Circle:
            if self.radius != other.radius:
                return True
            return False

    def __ge__(self, other):
        if type(other) == Circle:
            if self.radius >= other.radius:
                return True
            return False




circle1=Circle(radius=8)
circle2=Circle(diameter=12)
print(circle1,circle2,circle2>circle2,circle2==circle1,circle2!=circle1,circle2+circle1)
list_of_circles=[circle1,circle2]
print(list_of_circles)
list_of_circles.sort()
print(list_of_circles)