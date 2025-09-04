class Rectangle:
    def __init__(self, width = float, height = float):
        self.width = width 
        self.height = height

    def area(self):
        area_of_rectangle = self.width*self.height
        print(area_of_rectangle)

    def perimeter(self):
        per_of_rectangle = (2*self.width) + (2*self.height)
        print(per_of_rectangle)

width = eval(input("Enter width of the rectangle: "))
height = eval(input("Enter height of the rectangle: "))

new_rectangle = Rectangle(width , height)

new_rectangle.area()
new_rectangle.perimeter()