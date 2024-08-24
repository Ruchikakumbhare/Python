# Duck Typingg
#----------- Program1
# Polymorphism  poly ---many ,,morphism --one thing

class human:
    # mehod
    def talk(self):
        print('Hello i am human')
        
class duck:
    def talk(self):
        print('Quack Quack!!!')

# function
def call_talk(obj):
    obj.talk()
    
a1 = human()
a2 = duck()

call_talk(a1)  #Hello i am human
call_talk(a2)   #Quack Quack!!!

#----------- program2 (This is not the correct way)
# class human1:
#     def talk(self):
#         print('Helloo')
# class duck1:
#     def talk(self):
#         print('Quack')
# class dog:
#     def bark(self):
#         print('Bow Bow')
# def call_talk(obj):
#     obj.talk()
    
# x = human1()
# y =duck1()
# z =dog()
# call_talk(x)
# call_talk(y)
# call_talk(z) #error

#----------Program3
class human1:
    def talk(self):
        print('Helloo')
class duck1:
    def talk(self):
        print('Quack')
class dog:
    def bark(self):
        print('Bow Bow')
def call_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    else:
        obj.bark()
    
x = human1()
y =duck1()
z =dog()
call_talk(x)
call_talk(y)
call_talk(z)