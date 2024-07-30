
# #.......................................STRING.................................................

# color = "BLACK"
# print(color)
# print(len(color))      #5
# print(color[0])        #B

# #for range

# for char in range(len(color)):
#    # print(char)               #index
#     print(color[char])         #one by one

# #without range
# for x in color:
#     print(x)      

# #while loop
# a = 0
# while(a<(len(color))):
#     print(color[a])
#     a=a+1


#....................string Methods........................................
# upper(),lower(),captalize(),isupper(),istitle(),startswith(),endswith(),isdecimal(),isalpha(),isalnum()

#program1
name = "rUCHIKa"
a =name.upper()
print(a)                  #RUCHIKA

a1=name.lower()
print(a1)                 #ruchika

a2=name.capitalize()
print(a2)                 #isse lettr formet main aaye proper way main Ruchika

#program2
name1="RUCHIKA"
a3=name1.isupper()
print(a3)                  #TRUE     pura string capital to true


#program3
name2 = "Ruchika is very good girl"
a4=name2.istitle()
print(a4)                 #False              q ki sare first lettr capital nahi hai

nam = "Very Good"
a5=nam.istitle()
print(a5)                 #True

a6 =nam.startswith("ver")
print(a6)                 #false because of v-diff

a7=nam.startswith("Ver")
print(a7)                 #True


#program4

num = "123456"
x=num.isdecimal()
print(x)                    #True

num1 = "12345RK"
x1=num1.isdecimal()
print(x1)                   #False


#program5

fruit = "mango"
y=fruit.isalpha()
print(y)                    #true

fruit1 = "mango12"
y1=fruit1.isalpha()
print(y1)                  #False

z=fruit1.isalnum()
print(z)                   #True

str13 = "rk12345"
str14 = "ruchi"
str15 = "567"

print(str13.isalnum())    #true
print(str14.isalnum())    #true
print(str15.isalnum())    #true
