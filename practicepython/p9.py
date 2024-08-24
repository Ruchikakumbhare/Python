# instance method

# class person:
#     def __init__(self,fn,ln,ag):
#         self.fname = fn
#         self.lname = ln
#         self.age = ag
        
#     def display_n(self):
#         print(self.fname + self.lname)
    
#     def update(self,ag):
#      self.age = ag
# a1 =person("ruchika","kumbhare",22)
# print(a1.fname)
# print(a1.lname)
# print(a1.age)
# a1.update(21)
# print(a1.age)
# a1.display_n()


# class human:
#     def __init__(self,fn,ln,ag):
#         self.fname = fn
#         self.lname =ln
#         self.age =ag
#     def display_N(self):
#         print(self.fname + self.lname)
#     def updateage (self,ag):
#         self.age = ag
# x =human("ruchika","kumbhare",12)
# x.display_N()
# print(x.fname)
# print(x.lname)
# print(x.age)
# x.updateage(22)
# print(x.age)

# ------------------------------------------------------------------------------------
# INSTANCE METHOD

class person:
    def __init__(self,fn,ln,ct):
        self.fname = fn
        self.lname = ln
        self.city = ct
    def display_N(self):
        print(self.fname + self.lname)
    def changefname(self,fnn):
        self.fname = fnn
x =person("RUchi","Kumbhare","Nagpur")
print(x.fname)
print(x.lname)
print(x.city)
x.display_N()
x.changefname("Ruchikaa")
print(x.fname)
x.display_N()

# class method

class person1:
    city = "Nagpur"
    def __init__(self,fn,ln):
        self.fname = fn
        self.lname = ln
    def display(self):
        print(self.fname + self.lname)
    @classmethod
    def changecity(cn,ct):
        cn.city = ct
a = person1('Priya',"TArale")
a.display()
print(a.fname)
print(a.lname)
print(a.city)
a.changecity("Pune")
print(a.city)