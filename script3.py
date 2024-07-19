 #program 6

# tenary 


a = 20
b = 10
print("a is greater") if a > b else print(" b is greater")

num = 25
x = "yes u are" if num > 22 else "you are not"
print(x)

# for loop 16/07/24

# print 0 to 4 number
for x in range (5):
    print(x)
    
    
# print 1 t0 9
for x in range(1,10):
    print(x)
    
# print table of 2
for x in range(2,21,2):
    print(x)
    
#print revrese number 5 to 1
for x in range(5,0,-1):
    print(x)
    
#print reverse table of 5
for x in range(50,0,-5):
    print(x)

#break statement for loop

for x in range(6):
    print(x)
    if x == 3:
        break                # 0 1 2 3 
    
for x in range(7):
    if x ==3:
        break
    print(x)                 # 0 1 2 

for x in range(10,5,-1):
    if x ==8:
        break
    print(x)                # 10 9 
    
    
# print 1 to 10
for x in range(1,11):
    print(x)
    
for x in range(10,0,-1):
    print(x)
 


# while loop 17/07/24

a = 1
while(a<=5):
    print(a)
    a = a + 1    # 1 to 5
    
b = 5
while(b>=0):
    print(b)
    b=b-1
    
# table of 2
x = 2
while(x<=20):
    print(x)
    x = x+2
    
#reverse table of 3

y = 30
while(y>=3):
    print(y)
    y = y -3
    
x1 = 1
while(x<=7):
    print(x1)
    x1 = x1+1