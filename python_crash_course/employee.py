class Employee:
    def __init__(self,first, last, salary):
        self.first = first
        self.last = last
        self.salary = int(salary)
    
    def give_raise(self, raisesalary=5000):
        self.salary += raisesalary
        print(self.salary)

marek = Employee("marek", "chaler", "12000")
marek.give_raise(13000)


