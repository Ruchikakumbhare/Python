# # python object object ====> binary ------serialization
# # binary object        ====> python object ------- deserialization

# ------------------------------------------------------------------------------------------------------------
# -----------------------------------------Program1-----------------------------------------------------------
# class emp:
#     def __init__(self,fn,ln) -> None:
#         self.fname = fn
#         self.lname = ln
#     def display(self):
#         print(self.fname + self.lname)

# import pickle
# f = open('emp.dat','wb')
# n =int(input('enter the no of student'))
# for x in range(n):
#     fn =input('enter fname : ')
#     ln = input('enter lname : ')
#     c = emp(fn,ln)
#     pickle.dump(c,f)
# f.close()

# f = open('emp.dat','rb')
# while True:
#     try:
#         e = pickle.load(f)
#         e.display()
#     except EOFError:
#         print('end of the file')
#         break

# ------------------------------------------------------------------------------------------------------------
# -----------------------------------------Program2-----------------------------------------------------------

x1 = 10
with open('ct.bin','wb')as f:
    n = int(input('plz enter the no of cities'))
    for i in range(n):
        ct = input('plz enter city name  :  ')
        ct = ct+(x1 -len(ct))* "  "
        ct = ct.encode()
        f.write(ct)


# ------------------------------------------------------------------------------------------------------------
# -----------------------------------------Program3-----------------------------------------------------------

import os 
relen = 10
position = 0 
size  = os.path.getsize('ct.bin')
n = int(size/relen)
with open('ct.bin','rb')as f :
    for i in range(n):
        f.seek(0)
        str = f.read(10)
        str = str.decode()
        print(str)
        position = position + relen 

        






























