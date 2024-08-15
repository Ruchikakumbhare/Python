class Student:
    fname = 'riya'
    lname = 'sharma'
    age = 22
    
    def display_name(self):
        print(self.fname + self.lname)
        
class Teacher(Student):
    sal = 20000
    def displaysal(self):
        print(self.sal)
        
x = Teacher()
print(x.age)
print(x.fname)
print(x.lname)
x.display_name()
x.displaysal()