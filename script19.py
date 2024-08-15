#======================================= instance method==============================

class person :
    def __init__(self,fn,ln,ag) :
        # instance variables
        self.fname = fn
        self.lname = ln
        self.age =ag
        # instance method to print fullName
    def display_Name(self):
        print(self.fname + self.lname)
        
        # instance method to update age
    def updateage(self,ag):
           self.age = ag
a1 = person('Ruchika','Kumbhare',22)
print(a1.fname)
print(a1.lname)
a1.display_Name()
a1.updateage(21)
print(a1.age)
#===========================================================================================
# class method 
class person1 :
    country = 'india'  #---------------> # class level variable
    def __init__(self,fn,ln,ag):
        self.fname = fn
        self.lname = ln 
        self.age = ag
         
    def display_name(self):
        print(self.fname + self.lname)

    @classmethod
    def changecountry(cls,cn):
        cls.country = " Bharat"

ruchi = person1('ruchika','kumbhare',22)
print(ruchi.fname)
print(ruchi.lname)
print(ruchi.age)
print(ruchi.country)
ruchi.display_name()
ruchi.country='bharat'
print(ruchi.country)

# static method
# static methods are called directly on className

class Counter:
    # class variable
    count = 0
    # constructor
    def _init_(self):
        Counter.count =   Counter.count  + 1

    @staticmethod
    def countObj():
        return Counter.count
    
amol = Counter()
chinmay = Counter()

e = Counter.countObj()
print(e)