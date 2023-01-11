class Students:
    #initialize the properties
    def __init__(self, name= ".", age= ".", grade="."):
        self.name = name
        self.age = age
        self.grade = grade

    def print_name(self):
        print("Name: ", self.name)
        return self

    def print_age(self):
        print("Age: ", self.age)
        return self

    def print_grade(self):
        print("Grade:", self.grade)
        return self

    def print_all_info(self):
        self.print_name().print_age().print_grade()
        return self

#create object
raj = Students("raj")
raj.age = "21"
raj.print_all_info()


