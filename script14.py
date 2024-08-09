#.............program1
class student:
    fname = None
    lname = None
    age = None
    def display_name(self):
        print(self.fname+self.lname)
    
add = student()
print(add.fname)
add.fname = "ruchika"
add.lname = "kumbhare"
add.age= 22
print(add.fname)
print(add.lname)
print(add.age)

# ...............program 2             
#Setting the value at the time of object creation
class student1:
    def __init__(self,fn,ln,ct):
        self.fname = fn
        self.lname =ln
        self.city =ct
    def displayName(self):
        print(self.fname + self.lname)
add1 = student1("anushka","sharma","pune")
print(add1.fname)
print(add1.lname)
print(add1.city)

# program 3
class stud2:
    city = "mumbai"
    def __init__(self,fn,ln):
        self.fname = fn
        self.lname = ln
    def displayName(self):
        print(self.fname +self.lname)
    def changeCountry(self,ab):
        self.city(ab)
add2 = stud2("riya","parate")
add3 = stud2("pinki","parte")
print(add2.fname)
print(add2.lname)
print(add3.fname)
print(add3.lname)
print(add2.city)
print(add3.city)

#     def changeCountry(self,nc):
#         self.country = nc

# amit =  PersonC("amit","bhure")
# amit2 =  PersonC("amit2","bhure2")
# print(amit.firstName)
# print(amit.lastName)
# print(amit.country)

# print(amit2.firstName)
# print(amit2.lastName)
# print(amit2.country)

# amit2.changeCountry("bharat")
# print(amit2.country)
# print(amit.country)

# # instance 

# # class methods 

# # static methods