class Student:
    def __init__(self, name, year, section):
        self.name = name
        self.year = year
        self.section = section

    def details(self):
        print(f"Student name: {self.name}")
        print(f"Student year: {self.year}")
        print(f"Student section: {self.section}")


class Grade(Student):
    def __init__(self, name, year, section):
        super().__init__(name, year, section)
        self.subjects = ["science", "maths", "english"]
        self.marks = []
        self.total = 0
        self.avg = 0
        self.mark = 0
        self.grade = ""

    def calculate(self):
        for i in range(len(self.subjects)):
            self.mark = int(input("Enter marks in "+str(self.subjects[i])+ ": "))
            self.marks.append(self.mark)
        for i in range(len(self.marks)):
            self.total += self.marks[i]

        self.avg = self.total / 3
        if self.avg >= 80:
            self.grade = "A"
            print(f"Your grade is {self.grade}")
        elif self.avg >= 60:
            self.grade = "B"
            print(f"Your grade is {self.grade}")
        elif self.avg >= 40:
            self.grade = "C"
            print(f"Your grade is {self.grade}")
        else:
            print("Sorry!! You have failed.")


student1 = Grade("Joanna", 7, "A")
student1.details()
student1.calculate()
