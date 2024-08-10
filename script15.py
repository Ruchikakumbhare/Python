
#basic function
def no(x,y):
    return x+y
a=no(10,20)
print(a)

#.............. lamdba function 

# lambda --- keyword
# x , y  --- parameter 
# x + y  --- return type 
#......................Program1
a1 =lambda x,y:x+y
c=a1(10,30)
print(c)


add = lambda a,b:a+b
z1=add(100,200)
print(z1)

#.....................program 2

add1 = lambda a,b:a*b
x=add1(2,3)
print(x)

#..................... program 3
# function as parameter to another 
add2 =lambda a,b:a-b
def sub(fn,a,b):
    # fn =lambda a,b:a-b
    # a = 10
    # b = 10
    z=fn(a,b)
    return z
e=sub(add2,50,10)
print(e)

add3 =lambda x,y:x*y
def mul(fn,x,y):
    # fn=lambda x,y:x*y
    # x = 20
    # y = 10
    z = fn(x,y)
    return z
b=mul(add3,40,10)
print(b)


#........................Program4
# function as a return type 
def division():
    return lambda x,y:x/y
e = division()
e  = lambda x,y:x/y
print(e)
print(e(12,4))