
# # program 1: single inheritance - parent contructor , child no contructor

# class student:
#     fname = "Priyanka"
#     lname = "Sarwa"
#     city = "Mumbai"
    
#     def display_N(self):
#         print(self.fname  +  self.lname)
        
# class Teacher(student):
#     country = " india"
#     def display_c(self):
#         print(self.country)

# x = Teacher()
# x.display_c()
# x.display_N()


# # program 2:  single inheritance - parent contructor , child  contructor

# class Student1:
#     def __init__(self,fn,ln):
#         self.fname = fn
#         self.lname = ln
        
#     def display(self):
#        print(self.fname + self.lname)
       
# class Teacher1(Student1):
#     def __init__(self, fn, ln,sal):
#         super().__init__(fn, ln)     
#         self.salary = sal
#     def displaysal(self):
#         print(self.salary)
        
# x1 = Teacher1('Ruchika','Kumbhare',12000)
# x1.displaysal()
# x1.display()


# #program 3 :multi-level Inheritence
# class GrandFather:
#     def __init__(self,fn,ln):
#         self.fname = fn
#         self.lname  = ln
        
#     def display(self):
#         print(self.fname + self.lname)
        
# class Father(GrandFather):
#     def __init__(self, fn, ln,ag):
#         super().__init__(fn, ln)
#         self.age = ag
#     def dispalyag(self):
#         print(self.age)

# class Son(Father):
#     def __init__(self, fn, ln, ag,sal):
#         super().__init__(fn, ln, ag)
#         self.salary = sal
#     def displaysal(self):
#         print(self.salary)
        
# x2 = Son('sanskar','Gupta',45,2000)
# x2.dispalyag()
# x2.displaysal()


class GrandF:
    def __init__(self,gfn,ln) :
        self.gname = gfn
        self.lname = ln
        
    def display_gn(self):
        print(self.gname + self.lname)

class father(GrandF):
    def __init__(self, gfn, ln,fn):
        super().__init__(gfn, ln)
        self.fname = fn
    def display_fn(self):
        print(self.fname + self.lname)
    
class son(father):
    def __init__(self, gfn, ln, fn,sn):
        super().__init__(gfn, ln, fn)
        self.sname = sn
    def display_sn(self):
        print(self.sname + self.lname)

x3=son('sanchit','Sharma','Raghav','Arman')
print(x3.gname)
print(x3.lname)
print(x3.fname)
print(x3.sname)

x3.display_gn()
x3.display_fn()
x3.display_sn()






# # program 3
# # multilevel

# class GrandFather:
#     def _init_(self,fn,ln):
#         self.firstName = fn 
#         self.lastName = ln

#     def displayName(self):
#         print(self.firstName + self.lastName)


# class Father(GrandFather):
#     def _init_(self,fn,ln,ffn):
#         super()._init_(fn,ln)
#         self.fname = ffn
    
#     def displayFName(self):
#         print(self.fname + self.lastName)

# class Son(Father):
#     def _init_(self, fn, ln, ffn,ssn):
#         super()._init_(fn, ln, ffn)
#         self.sname = ssn

#     def displaySname(self):
#         print(self.sname + self.lastName)

# chinmay = Son("manohar","deshpande","shirish","chinmay")
# print(chinmay.firstName)
# print(chinmay.lastName)
# print(chinmay.sname)
# print(chinmay.fname)

# chinmay.displayFName()
# chinmay.displayName()
# # chinmay.displaySname()