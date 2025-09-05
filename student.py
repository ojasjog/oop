class Student:
    def __init__(self, name, grades=None):
        if grades is None:
            grades = []
        self.name=name
        self.grades=grades

    def new_grade(self, new:int):

        
        self.grades.append(new)
        

    def avg(self):
        average=sum(self.grades)/len(self.grades)
        print(f"The average of the {student.name}'s marks is {average}")

student = Student("Ojas", [])


n=eval(input(f"Enter the number of subjects graded for {student.name}: "))
i=0


while i <n:
    j=eval(input("Enter marks: "))
    student.new_grade(j)
    i+=1

student.avg()
print(f"All the marks of {student.name} are {student.grades}")
