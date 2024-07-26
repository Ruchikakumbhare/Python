#.......................tuple()................................25/07

info = ("riya",'ridhi','sidhi',"meena")#------------------------> tuple
print(info)
print(len(info))
print(type(info)) # <class 'tuple'>

info1 = "ruchika","neha","kritika","ritika","ridhi"
print(info1)
print(type (info1)) #<class 'tuple'>

print("kritika" in info) #false
print("ruchika" in info1) #True


color = 'red','pink','green','black','yellow','white'
print(color[0])                                       #tuple stores the index values

#range loop
for x in range(len(color)):
    print(color[x])              #all color print one by one
    
#without range
for x in color:
    print(x)                      #all color print one by one
    
#while loop
a = 0
while(a<len(color)):
    print(color[a])
    a =a+1
 
color2="pink","purple","blue","black"
#color2[3]="white"                        #tuples main direct update nhi ho skta so we convert tuple in list
color2=list(color2)
color2[2]="white"
print(color2)                              #['pink', 'purple', 'white', 'black']   convert list main kiya 
 
# two methods only 1) count          2) index
 
color2="pink","purple","blue","black","blue","blue"
a =color2.count("blue")
print(a)                                          #3

a1=color2.index("pink")
print(a1)                                         #0

#unpacking
x = (100,200,300,400)
a,b,c,d = x
print(a)
print(b)
print(a)
print(a)






 

    

