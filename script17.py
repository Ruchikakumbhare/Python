# class Person:
#     first_name  = None
#     last_name = None
#     age = None
#     rollNo = None

#     def display_name(self):
#         print(self.first_name + self.last_name)

# amol = Person()
# # print(amol.first_name)
# # print(amol.last_name)
# # print(amol.age)
# # print(amol.rollNo)
# #amol.display_name()

# # amol.first_name = "amol"
# # amol.last_name = "rao"
# # amol.rollNo = 23
# # amol.age = 34
# # amol.display_name()


# # program 2
# # Setting the value at the time of object creation

# class Person2:

#     # constructor
#     def _init_(self,fn,ln,ag,rn):
#         self.firstName = fn 
#         self.lastName = ln 
#         self.age = ag
#         self.rollNo = rn

#     def displayName(self):
#         print(self.firstName + self.lastName)

# amolD = Person2("amolD","raoD",34,55)
# print(amolD.firstName)
# print(amolD.lastName)
# print(amolD.age)
# print(amolD.rollNo)


# # program 3

# class PersonC:
#     country = "India"
#     def _init_(self,fn,ln):
#         self.firstName = fn 
#         self.lastName = ln

#     def display_name(self):
#         print(self.firstName + self.lastName)

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