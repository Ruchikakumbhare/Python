# set1 = {20,44,60,50}
# set2 = {30,50,40,60}

# a=set1.union(set2)  
# print(a) #{20,44,60,50,30,40}

# a1=set1.intersection(set2)
# print(a1) #{60,50}

# set1.intersection_update(set2)
# print(set1) #{50, 60}

# a2=set1.symmetric_difference(set2)
# print(a2)  #{30,40}

# set1.symmetric_difference_update(set2)
# print(set1)  #{40, 30}

# a11 = {10,203,50}
# a22 ={25,50,34}
# print(a11.difference(a22))#{10, 203}
# print(a22.difference(a11))#{25, 34}


# print(a11.isdisjoint(a22)) #False

# print(a11.issubset(a22))#false
# print(a11.issuperset(a22))#False

# no = {20,30,40}
# no1 = {30,40}
# print(no.issubset(no1)) #no ke sare elements no1 main nhi hai ths why false
# print(no.issuperset(no1)) #true  






number = {22,11,44,66,88}
number1 = {33,60,100}
x=number.union(number1) #22,11,44,66,88,33,60,100
print(x)

x1=number.intersection(number1)
print(x1)

x2=number.difference(number1)
print(x2)

x3=number.symmetric_difference(number1)
print(x3)