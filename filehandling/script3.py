# program 1 (not understand) class hi nhi kiya beta
# # f1 = open('dont.img.jpg','rb')
# f2 = open('dont.img.jpg','wb')
# # bytes = f1.read()
# f2.write(bytes)
# # f1.close()
# f2.close()

# -------------------------------------------------------------------------
# program 2
# with open('f1.txt','w') as f:
#     f.write("helloooo......")
#     f.write("byee.......")

# with open('f1.txt','r') as f:
#     a=f.read()
#     print(a)



# ---------------------------------------------------------------------------
# program 3
# python object -----> binary file ---- serialization
# binary object -----> python object ---- deserialization

# class student:
#     def __init__(self,fn,ln):
#         self.fname = fn
#         self.lname =ln 
#     def display_n(self):
#         print(self.fname + self.lname)

# import pickle
# f=open('stu.data','wb')
# a = int(input('number of object : '))

# for x in range(a):
#     fn = input('enter fname : ')
#     ln = input('enter lname : ')
#     z=student(fn,ln)
#     pickle.dump(z,f)
# f.close()

# -----------------------------------------------------------------------------
# program 4
class teachers:
    def __init__(self,fn,ln) -> None:
        self.fname = fn
        self.lname = ln 
    def display(self):
        print(self.fname + self.lname)

import pickle
f=open('stu.data','wb')
a = int(input('number of object : '))

for x in range(a):
    fn = input('enter fname : ')
    ln = input('enter lname : ')
    z=teachers(fn,ln)
    pickle.dump(z,f)
f.close()








f = open('stu.data','rb')
while True:
    try:
        e = pickle.load(f)
        e.display()
    except EOFError:
        print('end of the file')
        break
    
#-----------------------------------------------------------------------

l1 = 10
with open('name.bin','wb') as f:
    x=int(input('enter the number of name'))
    for i in range(x):
        name = input('enter the names : ')
        name = name +((l1 - len(name))) * " "
        name = name.encode()
        f.write(name)






























