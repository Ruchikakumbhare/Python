# class Student:
#     fname = 'riya'
#     lname = 'sharma'
#     age = 22
    
#     def display_name(self):
#         print(self.fname + self.lname)
        
# class Teacher(Student):
#     sal = 20000
#     def displaysal(self):
#         print(self.sal)
        
# x = Teacher()
# print(x.age)
# print(x.fname)
# print(x.lname)
# x.display_name()
# x.displaysal()

# single inheritance

class Emp :
    def __init__(self,fn,ln):
        self.fname = fn
        self.lname = ln
    def display_n(self):
        print(self.fname + self.lname)
class boss(Emp):
    def __init__(self, fn, ln,sal):
        super().__init__(fn, ln)
        self.salary = sal
        
    def display_S(self):
        print(self.salary)
        
x = boss('Ritika','sharma',10000)
print(x.fname)
print(x.lname)
print(x.salary)
x.display_n()
x.display_S()

# herarcial Inheritance

class grandM:
    def __init__(self,gmn,ln):
        self.grandname = gmn
        self.lname = ln
    def display(self):
        print(self.grandname + self.lname)
        
class son(grandM):
    def __init__(self, gmn, ln,sn):
        super().__init__(gmn, ln)
        self.sname = sn
    def display_Son(self):
       print(self.sname)
       
class daughter(grandM):
    def __init__(self, gmn, ln,dn):
        super().__init__(gmn, ln)
        self.dname = dn
    def display_d(self):
        print(self.dname)
y1 = son('savita','Verma','shobit')       
y = daughter('savita','Verma','saniya')
print(y.dname)
print(y1.sname)

# multilevel inheritance

class grandf:
    def __init__(self,gfn,ln):
        self.gfname =gfn
        self.lname = ln    
    def display_g(self):
       print(self.gfname + self.lname)
       
class father(grandf):
    def __init__(self, gfn, ln,fn):
        super().__init__(gfn, ln)
        self.fname = fn
    def display_fa(self):
       print(self.fname + self.lname)
       
class son(father):
    def __init__(self, gfn, ln, fn,snn):
        super().__init__(gfn, ln, fn)
        self.ssname = snn
    def display_snn(self):
       print(self.ssname + self.lname)   
       
i1 = son('vishal','Tiwari','vikram','vihan')
print(i1.gfname)
print(i1.ssname)
print(i1.fname)
print(i1.lname)
i1.display_g()
i1.display_fa()
i1.display_snn()