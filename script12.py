
#program1
num1 = {1,2,4,5}
num2 ={2,3,5,6}
a=num1.union(num2)
print(a)                   #combine 2 sets and create new set  {1, 2, 3, 4, 5, 6}

#program2
num3 = {10,30,40,50,60}
num4 = {10,30}
b=num3.intersection(num4)
print(b)                  #common of both  {10, 30}

num3.intersection_update(num4)
print(num3)                   #{10, 30}


#program3
num5 = {100,200,40,50,33,66}
num6 = {25,66,50}
d=num5.difference(num6)
print(d)            #{200, 33, 40, 100}    num 5 main diff check krnga
d=num6.difference(num5)
print(d)            #{25}

num5.difference_update(num6)
print(num5)

#program4
no = {36,10,55,80,83,90}
no1 = {22,30,70,90,80,83}

print(no.isdisjoint(no1)) #same rhe to false

setH1 = {66,77}
setH2  = {88,55,33}
print(setH1.isdisjoint(setH2))   #diff rhe to true

#program5
num5 = {100,200,40,50,33,66}
num6 = {25,66,50}
l=num5.symmetric_difference(num6)
print(l)                                   #ismain  same value chod denga {100,200,40,25,33}

num5.symmetric_difference_update(num6)
print(num5)

#program6


setN = {11,22}
setM = {11,22,33,66}

print(setN.issubset(setM))
print(setM.issuperset(setN))