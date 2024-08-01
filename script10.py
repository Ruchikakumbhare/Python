#..................................................set...................................................

# list = []
# dict = {}
# tuple = ()
# set ={}

#set does not store index values
set = {10,20,30,40,50}
print(set)              #{50, 20, 40, 10, 30}
print(type(set))        #<class 'set'>
print(len(set))          #5
print(30 in set)         #True

for x in set:
    print(x)           # one by one no.
    
#.......................................set methods......................................

# add(),clear(),copy(),pop(),remove(),update()
#add
set1 = {"ruchi","riya","preety"}
set1.add('neha')
print(set1)        #{'preety', 'riya', 'neha', 'ruchi'}         

#clear
# set1.clear()
# print(set1)          #set()
    

#copy
nam = {'ruchi','neha','priya','astha'}
nam1= nam
nam1.add('pinky')
print(nam1)#{'neha', 'priya', 'pinky', 'astha', 'ruchi'}
print(nam) #{'neha', 'priya', 'pinky', 'astha', 'ruchi'}

nam1=nam.copy()
nam1.add('sonu')
print(nam1)      #{'priya', 'astha', 'ruchi', 'sonu', 'neha', 'pinky'}
print(nam)       #{'neha', 'priya', 'pinky', 'astha', 'ruchi'}

#pop
number = {10,20,30,40,55,33}
number.pop()
print(number)   # {20, 55, 40, 10, 30}

nam11 = {'ruchi','neha','priya','astha'}
nam11.pop()
print(nam11)         #{'neha', 'ruchi', 'priya'} koi bhi ek element pop hojynga

#remove
color ={'blue',"green"}
color.remove('blue')
print(color)       #{'green'}
    
nam11.update({'soniya','piniki'})
print(nam11)