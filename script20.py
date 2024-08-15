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





# class Student:
#     firstName = "chinmay"
#     lastName = "deshpande"
#     adharCard = 123

#     def displayName(self):
#         print(self.firstName + self.lastName)



# class Teacher(Student):
#     salary = 123123    
#     def displaySalary(self):
#         print(self.salary)

# amolT2 = Teacher()
# print(amolT2.firstName)
# print(amolT2.lastName)
# print(amolT2.adharCard)
# print(amolT2.salary)

# amolT2.displayName()
# amolT2.displaySalary()

# # program 1
# # single inheritance - parent contructor , child no contructor
# # single inheritance - parent contructor , child  contructor
# # multi-level
# # herarchical 
# # multiple

# # 7 pm