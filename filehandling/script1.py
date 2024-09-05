#file handling ----->read,write,append
#--------------------------------program1
# creating the object of file and opening in write mode

# a=open('first.txt','w')                      #creating the object of file and opening in write mode
# a.write("This is my first line of code")     # writing into the file
# a.close()                                    # closing the file

# #------------------------------- program 2
# # open the file in read mode
# a = open('first.txt','r')
# x=a.read()
# print(x)
# a.close()

#-------------------------------- program 3
# will overwrite the existing file
# a = open('first.txt','w')
# a.write('This is my second line of code')
# a.close()


#--------------------------------- program 4
# opening the file in append mode
# a = open('first.txt','a')
# a.write("hello i am learning python\n")
# a.close()


#--------------------------------- program 5 
# a = open('fisrt1.txt','+a')
# x1=input("please enter your name  \n")
# a.write(x1 + "\n")
# a.seek(0,0)
# x2=a.read()
# print(x2)
# a.close()


# ------------practice----------
# x=open('day.txt','w')
# x.write("Hii i am learning python")
# x.close()

# x=open('day.txt','r')
# x1=x.read()
# print(x1)
# x.close()

# x=open('day.txt','w')
# x.write("yes i am also learning js")
# x.close()

# x=open('day.txt','a')
# x.write("i am learning python\n")
# x.close()


