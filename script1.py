"""x = "ruchika"  # python comment """     """                          // jscomment /*.....*/

print(x)

print(type (x))

y = 10
#print (type(y))



a = 50
b = 10
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)


# function
def calcy(x, y):
    print(x + y)


calcy(20, 10)


# function without parameter and without return type

def number():
    print(10 + 100)


number()


# function with parameter and without return type

def number1(a, b):
    print(a + b)


number1(20, 20)
number1(70, 30)


# function with return type and with parameter
def number2(p, q):
    return p + q


z = number2(100, 500)
print(z)

a = True
print(type(a))

"""

for x in range(50,0,-1):
    print(x)

    
a = 50
while(a>=0):
    print(a)
    a=a-1