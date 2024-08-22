
# program 1: single inheritance - parent contructor , child  no contructor

class student:
    fname = "Priyanka"
    lname = "Sarwa"
    city = "Mumbai"
    
    def display_N(self):
        print(self.fname  +  self.lname)
        
class Teacher(student):
    country = " india"
    def display_c(self):
        print(self.country)

x = Teacher()
x.display_c()
x.display_N()


# program 2:  single inheritance - parent contructor , child  contructor

class Student1:
    def __init__(self,fn,ln):
        self.fname = fn
        self.lname = ln
        
    def display(self):
       print(self.fname + self.lname)
       
class Teacher1(Student1):
    def __init__(self, fn, ln,sal):
        super().__init__(fn, ln)     
        self.salary = sal
    def displaysal(self):
        print(self.salary)
        
x1 = Teacher1('Ruchika','Kumbhare',12000)
x1.displaysal()
x1.display()


#program 3 :multi-level Inheritence
class GrandFather:
    def __init__(self,fn,ln):
        self.fname = fn
        self.lname  = ln
        
    def display(self):
        print(self.fname + self.lname)
        
class Father(GrandFather):
    def __init__(self, fn, ln,ag):
        super().__init__(fn, ln)
        self.age = ag
    def dispalyag(self):
        print(self.age)

class Son(Father):
    def __init__(self, fn, ln, ag,sal):
        super().__init__(fn, ln, ag)
        self.salary = sal
    def displaysal(self):
        print(self.salary)
        
x2 = Son('sanskar','Gupta',45,2000)
x2.dispalyag()
x2.displaysal()

# exercise
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

# Program4 : Hierarchical inheritance

class mother:
    def __init__(self,mn,ln):
        self.mname = mn
        self.lname = ln
        
    def display(self):
        print(self.mname + self.lname)
class son(mother):
    def __init__(self, mn, ln,sn):
        super().__init__(mn, ln)
        self.sname = sn
    def display_s(self):
        print(self.sname)
class daughter(mother):
    def __init__(self, mn, ln,dn):
        super().__init__(mn, ln)
        self.dname = dn
    def display_d(self):
        print(self.dname)
        
w1 = son('Alka','Kumbhare','Rohit')
w2 = daughter('Shobha','Bhisikar','Payal')
print(w1.mname)
print(w1.lname)
print(w1.sname)
print(w2.dname)
w1.display()
w1.display_s()
w2.display_d()

