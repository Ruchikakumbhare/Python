year = [2002,2003]
age = []
for x in year:
    ag =2024-x
    age.append(ag)
print(age)

x1=(list(map(lambda x : 2024-x,year)))
print(x1)

# list comprehension
#[expression:loop:condition(only one condition)]
x2 =[2024-x for x in year]
print(x2)

x3=[2023-x for x in year]
print(x3)

x4=[2022-x for x in year]
print(x4)
# program 2
transactions = [9900,-1923,8000,4455,6666,-777,888,-444]

q=(list(filter(lambda x : x<0,transactions)))
print(q)
q1=[x<0 for x in transactions]
print(q1)


deposit = []
for x in transactions:
    if x > 0:
        deposit.append(x)
print(deposit)


# program 4 
no = [20,30,40]
total = 0
for x in no:
    total = total + x
print(total)

from functools import reduce
print(reduce(lambda acc,el : acc+el, no))




numbersB = [11,22,33,44]


evenOdd = []
for x in numbersB:
    if x % 2 == 0:
        evenOdd.append('even')
    else:
        evenOdd.append('odd')
print(evenOdd)


a = ["even" if x%2 ==0 else "odd" for x in numbersB]
print(a)
# e2 = ["even" if x % 2 == 0 else "odd" for x in numbersB]
# print(e2)


print([x * 2 for x in range(1,11)])

print([x*3 for x in range(1,11)])
for x in range(2,21,2):
    print(x)