
# blank object
class student:
    fname = None
    lname = None
    age = None
    add = None
    
    def walk(self):
        print("i am walking")
    
    def talk(self):
        print("i am taking")

# create object
ruchika = student()

# retriving the properties
print(ruchika.fname)
print(ruchika.lname)
print(ruchika.age)
print(ruchika.add)

ruchika.walk()
ruchika.talk()


#setting the prop values outside the class
ruchika.fname = "Ruchi"
ruchika.lname = "Kumbhare"
ruchika.age =22
ruchika.add =50
print(ruchika.fname)
print(ruchika.lname)
print(ruchika.age)
print(ruchika.add)

neha = student()
neha.fname = "neha"
neha.lname = "Tarale"
neha.age =23
neha.add =52
print(neha.fname)
print(neha.lname)
print(neha.age)
print(neha.add)

#constructor
class my:
    def __init__(self,fn,ln):
        self.fname = fn
        self.lname = ln
        
        def display_name(self):
            print(self.fname + self.lname)
    
rk = my("ruchika","kumbhare")
print(rk.fname) 


class person:
    def __init__(self,fn,ln,ag,ct) :
        self.fname = fn
        self.lname = ln
        self.age = ag
        self.city = ct
        
        def display_name(self):
            print(self.fname  + self.lname)

riya =person("riya","sharma",22,"pune")
print(riya.fname)
print(riya.lname)
print(riya.age)
print(riya.city)

#riya.display_name()


class name:
    def __init__(self,ct,no,add):
        self.city = ct
        self.number=no
        self.address=add
        def display_Name():
            print(self.fname + self.lname)
            
a1 = name("pune",123,"wathoda")
a1.fname = "soni"
print(a1.fname)
print(a1.city)

a1.display_Name()