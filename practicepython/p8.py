#single  inheritance
class student:
    def __init__(self,fn,ln):
        self.fname = fn
        self.lname = ln
    def display(self):
        print(self.fname + self.lname)
        
class Teacher(student):
    def __init__(self, fn, ln,stn):
        super().__init__(fn, ln)
        self.stname = stn
    def display1(self):
        print(self.stname)
        
a1 =Teacher('SOnil','Gupta','Aanvil')
print(a1.fname)
print(a1.lname)
print(a1.stname)
a1.display()
a1.display1()

#multi-level inheritance
class grandfather:
    def __init__(self,gfn,ln):
        self.gname = gfn
        self.lname = ln
class father(grandfather):
    def __init__(self, gfn, ln,fn):
        super().__init__(gfn, ln)
        self.fname =fn
class son(father):
    def __init__(self, gfn, ln, fn,sn):
        super().__init__(gfn, ln, fn)
        self.sname = sn

x = son('swapnil','wankhede','rohan','roshan')
print(x.fname)
print(x.gname)
print(x.sname)

#hirarchical

class gmother:
    def __init__(self,gm,ln):
        self.gmname =gm
        self.lname =ln
class son(gmother):
    def __init__(self, gm, ln,sn1):
        super().__init__(gm, ln)
        self.snname =sn1
class daughter(gmother):
    def __init__(self, gm, ln,dn):
        super().__init__(gm, ln)
        self.dname = dn
x2 =daughter('leela','Trale','Neha')
x3= son('leela','tarale','mohan')
print(x2.dname)
print(x2.gmname)
print(x3.snname)


