from abc import ABC, abstractmethod

class Shape_Area(ABC):
    @abstractmethod
    def getArea(self, sides, num1, num2):
       pass

class Circle(Shape_Area):
    def getArea(self, sides, num1, num2):
        print(3.14 * (pow(num1, 2)))
    
class Square(Shape_Area):
    def getArea(self, sides, num1, num2):
        print(pow(num1, 2))

class Rectangle(Shape_Area):
    def getArea(self, sides, num1, num2):
        print(num1 * num2)        



class Shapes:
    def __init__(self,  sides, num1, num2 ):       
        self.sides = sides
        self.num1 = num1
        self.num2 = num2

    def getArea(self, shapeArea):
         shapeArea.getArea(self.sides, self.num1, self.num2)


def main():
  item1 = Shapes( 0, 1, 0)
  item2 = Shapes( 4, 3, 2)
  
  item1.getArea(Circle())
  item2.getArea(Rectangle())


if __name__ == "__main__":
    main()