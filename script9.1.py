#practice of string

# month = "january"
# print(month)
# print(len(month))
# print(month[5])


# month = "january"
# #for in range
# for char in range(len(month)):
#     print(month[char])
#     print(char)

# #without range
# for x in month:
#     print(x)
    
# #while loop
# a = 0
# while(a<len(month)):
#     print(month[a])
#     a=a+1

month = "JanuarY"
a=month.upper()
print(a)

a1=month.lower()
print(a1)


#.............................

mon = "augest"
a2=mon.capitalize()
print(a2)

a3=mon.isupper()
print(a3)

a4=mon.istitle()
print(a4)


a5=mon.startswith('aug')
print(a5)

a6=mon.endswith("st")
print(a6)

#..............................
mon1= "123456"
a7=mon1.isdigit()
print(a7)

mon2="qwerty"
a8=mon.isalpha()
print(a8)

mon3="123asd"
a9=mon3.isalnum()
print(a9)

#..............................

a1 = "12345"
a2 ="asdf"
a3 ="123asd"

x=a1.isalnum()
x1=a2.isalnum()
x2=a3.isalnum()