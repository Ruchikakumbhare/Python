# inheritance 

class student:
    fname = "Ruchika"
    lname = "Kumbhare"
    
    def displayN(self):
        print(self.fname + self.lname)

class Teacher(student):
    salary = 10000
    def displaysal(self):
        print(self.salary)

a1 =  Teacher()
print(a1.fname)
print(a1.lname)
print(a1.salary)
a1.displayN()
a1.displaysal()




