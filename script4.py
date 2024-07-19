#...................... list

name = [ "Ruchika","Lalita","Meena","Divya"]
print(name)

# retreive
print(name[0])
print(name[3])

# update
name[1] = "Aruna"
print(name)
name[3] = "Supriya"
print(name)

#add - append
name.append("Gauri")
print(name)

#remove
name.remove("Supriya")
print(name)

print(type (name))




#.............Program1

names = ["Ruchika","Neha","Kanchan","Payal","Sneha"]
for x in range(len(names)):
    print(x)       #it will show length of list 0,1,2,3,4
    print(names[x])  # 0 ruchika 1 neha 2 kanchan 3 payla 4 sneha
    
for x in range(len(names)-1,-1,-1):
    print(x)       #reverse index
    print(names[x]) #reverse list


for x in range(len(names)-1,-1,-1):
    print(names[x])                    # reverse name print

#while loop
i = 0
while(i<5):
    print(names[i])
    i = i +1

 # without range()
fruits = ["apple","mango","grapes","banana"]
for x in fruits:
    print(x)



    
fruit = ["apple","mango","banana","kivi"]
for x in range(len(fruit)-1,-1,-1):
    print(fruit[x])


for x in range (0,4):
    print(x)

for x in range(len(fruit)):
    print(fruit[x])







