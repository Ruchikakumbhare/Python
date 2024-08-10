#profram1
class person :
    fname = None
    lname = None
    age = None
    
    def displayName(self):
        print(self.fname + self.lname)
        
stud = person()
print(stud.fname)
stud.fname = "Tejaswini"
print(stud.fname)

#Program2
class person1:
    def __init__(self,fn,ln,ag):
        self.fname = fn
        self.lname = ln
        self.age =ag
        def displayName(Self):
            print(self.fname + self.lname)
            
stud1 = person1("ritika","sarva",22)
print(stud1.fname)
print(stud1.lname)
print(stud1.age)

#program3
class person3:
    city = "MUmbai"
    def __init__(self,fn,ln):
        self.fname = fn
        self.lname = ln
        
        def displayName(Self):
            print(Self.fname + self.lname)
            
        def ChangeName(self):
            print(self.fname+self.lname)
stud2=person3("raj","kohli")
print(stud2.fname)
print(stud2.lname)
print(stud2.city)