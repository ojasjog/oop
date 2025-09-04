
name=input("Enter name of Dog: ")
age=int(input("Enter age of Dog: "))
class Dog:

    def __init__(self, name:str, age:int) -> None:
        self.name=name
        self.age=age

    def bark(self):
        print(f"{self.name} is barking! Woof!")

    def get_dog_years(self, years=int):
        years = self.age*7
        print(years)


D1 : Dog = Dog(name=name, age=age)


D1.bark()

D1.get_dog_years()
