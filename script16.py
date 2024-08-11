# program 1
birthy = [2002,2003,2004]
ages = []
for x in birthy:
    print(2024-x)         # one by one 22,21,20
    ag =2024-x
    ages.append(ag)
print(ages) #[22, 21, 20]
print(list(map(lambda x:2024-x,birthy))) #[22, 21, 20]

brYear = [1997,1998,1999,2000]
age = []
# for x in brYear:
#     ag =2024-x
#     age.append(ag)
# print(age)
print(list(map(lambda x:2024-x,brYear)))  #[27, 26, 25, 24]

#program 2
num = [10,20,40]
print(list(map(lambda x:x+10,num))) #[20, 30, 50]

# program 3
# filter 
marks = [40,25,10,60]
above30 = []
for x in marks:
    if x>30:
        above30.append(x)
    print(above30)            #[40, 60]
    
#using filter lambda 
a=(list(filter(lambda x:x>30, marks)))
print(a)

a2=(list(filter(lambda x:x<30,marks)))
print(a2)

#program 4
trans = [20,50,60,-30,7,-3,-6,90,-8,-10]
withrawl=(list(filter(lambda x:x<0,trans))) #[-30,-3,-6,-8,-10]
deposit=(list(filter(lambda x:x>0,trans)))
print(withrawl)
print(deposit)

# program 5
no = [100,200,300]
total = 0
for x in no:
    total =total + x
print(total)   #600

from functools import reduce
f=reduce(lambda acc,el:acc+el,no)
print(f)



number = [10,20,30,40]
add = 0
for x in number:
    add = add + x
print(add)  #100