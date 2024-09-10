# program 1-------------------------------------------------
# x =open('second.txt','w') #------>open the file
# x.write("hello!!!")
# x.close()

# program 2-------------------------------------------------
# x2=open('second.txt','r')
# print(x2.read())
# x2.close()

# program 3-------------------------------------------------
# x3=open('2.txt','w')
# st=input("ENTER YOUR NAME: \n") #-->input from users
# x3.write(st)                    #--->stoare input in opening file
# x3.close()

# program 4-------------------------------------------------
# x4=open('2.txt','r')
# st =x4.read() # read from the file
# print(st)     # console the content of file
# x4.close()


# program 5-------------------------------------------------
# user input for multiple names 
# when user input '@', exit the loop

# x5=open('name.txt','w')
# print('please enter "@" to exit')
# while(str!="@"):
#     str = input('please enter multiple name : ')
#     if str != "@":
#         x5.write(str +"\n") 
# x5.close()

# program 6-------------------------------------------------
# write and read 

x6=open('name2.txt','+a')
print('please enter the "*" from exit')
while(str!="*"):
    str = input ('please enter the number : \n')
    if str != "@":
        x6.write(str + "\n")
x6.seek(0,0)
str = x6.read()
x6.close()







