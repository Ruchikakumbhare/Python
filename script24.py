

# polymorphism
# duck typing 
# overloading 
# overriding 
# operator overload

#-------------------------- operator overloading

class BookA:
    def __init__(self,pages):
       self.pages = pages

    def _add_(self,others):
        return self.pages + others.pages
class BookB:
    def __init__(self,pages):
       self.pages = pages

    def _add_(self,others):
        return self.pages + others.pages

Cartton1 = BookA(50)
cartoon2 = BookB(100)
print(Cartton1.pages +cartoon2.pages )



# class BookX:
#     def _init_(self,pages):
#        self.pages = pages
    
#     # addition operator overloaded to get result of adding object
#     def _add_(self,others):
#         return self.pages + others.pages

# class BookY:
#     def _init_(self,pages):
#       self.pages = pages
#     def _add_(self,others):
#         return self.pages + others.pages
    

# mahabharat = BookX(120)
# ramayan = BookY(240)

# print(mahabharat.pages + ramayan.pages)
# print(mahabharat+ramayan)
# print(ramayan+mahabharat)


# class BookY:
#     def _init_(self,pages):
#       self.pages = pages

# class BookX:
#     def _init_(self,pages):
#        self.pages = pages

#     def _gt_(self,other):
#        return self.pages > other.pages 


# x = BookX(30)
# y = BookY(25)
# print(x.pages > y.pages)
# print(x > y)


#----------------------------------- abstraction

# from abc import ABC , abstractmethod
# class rbi(ABC):
#     @abstractmethod
#     def loan(self):
#         pass
#     def save(self):
#         pass
# class SBI(rbi):
#     def loan(self):
#         print("loan method")
# class pnb(rbi):
#     pass
# a = SBI()

# from abc import ABC , abstractmethod

# class Demo(ABC):
#    @abstractmethod
#    def loan(self):
#       pass
   
#    def save(self):
#       pass

# class SBI(Demo):
#    def loan(self):
#       print("loan method")

# class PNB(Demo):
#    pass

# a = SBI()


# continue

from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod 
    def  save(self):
     pass
    @abstractmethod
    def loan(self):
       pass

class oneBAnk(Bank):
    def save(self):
        print("save oneBank")
    def loan(self):
        print("loan onebank")
class twoBank():
    def save(self):
        print("save two bank")
    def loan(self):
        print("loan two bank")

b = oneBAnk()
c= twoBank()
b.save()
b.loan()
c.save()
c.loan()



from abc import ABC , abstractmethod
class customer(ABC):
    @abstractmethod
    def ser1(self):
        pass
    @abstractmethod
    def ser2(self):
        pass

class amezon(customer):
    def ser1(self):
        print("amazon service1")
    def ser2(self):
        print("amazon service2")
    

class flipcart(customer):
    def ser1(self):
        print("flipcart service1")
    def ser2(self):
        print("flipcart service2")

v1= amezon()
v2=flipcart()

v1.ser1()
v1.ser2()
v2.ser1()
v2.ser2()