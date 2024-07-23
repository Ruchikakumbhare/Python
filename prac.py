"""def num(x,y):
    print(x+y)
num(10,2)
num(50,50)   


def num1():
    print(10+10)
num1()

def num2(a,b):
    return a +b
e=num2(20,20)
print(e)
print(e*10)


print(5==5 and 6==6)
print(5!=7 or 5==5)


i = 80
if (i<50):
    print("c grade")
elif(i>70):
    print("b grade")
else:
    print("-a grade")



aa = "ruchi"
print(type (aa) )



#15/07/24 practice


m = "ruchika"
print(type (m)) #CLASS STRING

def my (m1,n1):  #para and without return
    print(m1*n1)
    print(m1+n1)
my(50,10)
my(20,10)

def my1():       #without para and without return type
    print(100+200)
my1()

def my2(m2,n2):
    return m2 + n2
l = my2(500,500)
print(l)
print(l+2000)


p = 50
if p<20:
    print("incoorect")
elif p>30:
    print("correct")
else:
    print("not possible")
    
    
#19/07/24

#for x in range(10):
 #   print(x)
 
list = ["Soniya","priya","diya"]
#for x in range(len(list)):
#    print(x)
   # print(list[x])
   
x = 2
while(x>=0):
    print(list)
    x = x-1
    
for x in range (len(list)-1,-1,-1):
    print(list[x])
    
    
name = [ "ruchika","soniya","meena"]
print(len(name))



#22/07


##using for loop
#print 0 to 9 using for loop

for x in range(10):
    print(x)
    
#print 5 to 15
for x in range(5,16):
    print(x)
    
#while loop
a = 1
while(a<=10):
    print(a)
    a=a+1
    
b = 10
while(b>=2):
    print(b)
    b=b-1
    
  
  
list = ["blue","green","purple","black","yellow"]
print(len(list))  
    
for x in range(len(list)):
    print(x)
    
for x in range(len(list)-1,-1,-1):
    print(x)
    
num = ["my","i","say"]
a = 0
while(a<3):
    print(num[a])
    a=a+1
    #while loop
"""

for x in range(11):
    print(x)

for x in range(2,16):
    print(x)


num = 10
while(num>1):
    print(num)
    num = num-1


list = ["mango","apple","grapes","banana","papaya"]
for x in range(len(list)):
    print(x)
for x in range(len(list)-1,-1,-1):
    print(x)

for x in list:
    print(x)

#22/07/24

#append
names = ["chaitanya","mangesh","apurva","adrsh","ankit","milind"]
names.append("Neha")
print(names)

#pop
names.pop()
print(names)
names.pop(2)
print(names)

#remove
names.remove("adrsh")
print(names)

#sort
names.sort()
print(names)

#reverse
names.reverse()
print(names)

#insert
names.insert(2,"neha")
print(names)

#extende
names.extend(["adarsh","Ruchika"])
print(names)

#index
a = names.index("Ruchika")
print(a)

#clear
names.clear()
print(names)

#copy
let1 = ["priya","sonu"]
let2=let1.copy()
let2[0]="supriya"
print(let1)
print(let2)

