# l1=open('pp1.txt','w')
# l1.write('Practice practice!!!!')
# l1.close()


# l1=open('pp1.txt','r')
# x=l1.read()
# print(x)
# l1.close()

# l1=open('pp1.txt','+a')
# l1.write("\n  hello hello hello!!1")
# l1.read()
# l1.close()

# x1=open('pp1.txt','w')
# x=input('ENter the NUmber : \n')
# print(x)
# x1.close()

x2=open('pp1.txt','w')
print('please enter "1" to exit ')
while(str!="1"):
    str = input('please enter multiple name : ')
    if str !="1":
        x2.write(str + "\n")
x2.close()
