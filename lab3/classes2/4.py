import math

class Point:
    def __init__(self, x, y):
        self.x=x
        self.y=y

    def show(self):
        print(f"Point coordinates: {self.x}, {self.y}")

    def move(self, new_x, new_y):
        self.x=new_x
        self.y=new_y
        print(f"Point moved to: {self.x}, {self.y}")

    def dist(self, other):
        return math.sqrt((self.x-other.x) ** 2 + (self.y-other.y) ** 2)
    
point1= Point(2 ,3)
point2= Point(5, 7)

point1.show()
point1.move(8, 10)
print(point1.dist(point2))