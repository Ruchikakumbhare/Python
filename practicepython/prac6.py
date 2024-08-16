def my(x,y):
    return x + y
z=my(10,20)
print(z)

#lambda function
a1 =lambda x,y:x+y
z1=a1(20,20)
print(z1)

a2=lambda x,y:x*y
z2=a2(10,20)
print(z2)

# function as parameter to another 
a3 = lambda x,y:x-y
def sub(fn,x,y):
    # fn = lambda x,y:x-y
    # x =20
    # y =10
    z=fn(x,y)
    return z
z3=sub(a3,50,20)
print(z3)

a4=lambda x,y:x*y
def mul(fn,x,y):
    # fn = lambda x,y:x*y
    # x = 100
    # y =200
    z =fn(x,y)
    return z
z4=mul(a4,200,100)
print(z4)




no = [2,4,6,8]
new = []
for x in no:
    if x % 2 ==0:
        new.append('even')
    else:
        new.append('odd')

print(new)

