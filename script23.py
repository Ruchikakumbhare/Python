# DUCK TYPING
class human:
    def talk(self):
        print("hiiiiiiieeee")
class cat:
    def talk(self):
        print("Meoww Meooww")
class dog:
    def bark(self):
        print("Bhow Bhoww")

def call_talk(obj):
    if hasattr(obj,"talk"):
        obj.talk()
    elif hasattr(obj,"bark"):
        obj.bark()
a = human()
b = cat()
c = dog()
call_talk(a)
call_talk(b)
call_talk(c)

# # overloading 
# ----------------
# # same class , same method but different signature 

# class Calculator:
#     # def addition(self,x,y):
#     #   print(x+y)

#     # def addition(self,x,y,z):
#     #   print(x+y+z)

#     # def addition(self,x,y,z,a):
#     #   print(x+y+z+a)  
# e = Calculator()
# e.addition(12,3)
# e.addition(12,3,3)
# e.addition(12,3,3,4) --------------------------THIS IS NOT CORRECT WAY TO ACHEVIE OVERLOADING 

class calcy:
    def addition(self, a1 =None, b1 = None,c1 = None,d1 = None):
        if a1!= None and b1!=None and c1!=None and d1!=None:
            print(a1+b1+c1+d1)
        elif a1!= None and b1!=None and c1!=None:
            print(a1+b1+c1)
        elif a1!= None and b1!=None:
               print(a1+b1)
x = calcy()
x.addition(5,5,5,5)
x.addition(5,5)
x.addition(5,5,5)


# overriding 
# ---------------
# same methodname , same signature but different class 
# has a relationship

# Program1
# class SBIBank:
#     def save(self):
#         print("save the bank")
#     def loan(self):
#         print("Loan from Bank")

# x1 = SBIBank()
# x1.save()
# x1.loan()

# Program2
class SBIBank:
    def save(self):
        print("save the bank")
    def loan(self):
        print("Loan from Bank")
class Kotak(SBIBank):
    def save(self):
        print("save the Kotakbank")
    def loan(self):
        print("Loan from KotakBank")
x1 = Kotak()
x1.save()
x1.loan()


# operator overloading

print(10+10)
print("Hello" + "Ruchi")
# print(2 + "hello")
# print("hello"+2)
# # print(obj + obj)