#........list methods
# 10 list methods
#append(),pop(),remove(),index(),sort(),extend(),reverse(),clear(),count(),insert()


#list = ["blue","red","green","pink","purple","black"]
#print(list)
#print(list[1])

#append  (add krna)
list = ["blue","red","green","pink","purple","black"]
list.append("Brown")
print(list)    #["blue","red","green","pink","purple","black","Brown"]

#pop (delete krna last element)
list.pop()
print(list)        # delete brown color           output: ["blue","red","green","pink","purple","black"]

list.pop(3)
print(list)        # delete 3 index element       output:['blue', 'red', 'green', 'purple', 'black']

#remove
list.remove("blue")
print(list)        # delete blue element           output :['red', 'green', 'purple', 'black']

#index
a = list.index("green")
print(a)           # element ka index return       output : 1

#insert
list1 = ["cupcake","chocalate","icecream","candy","cake"]
list1.insert(2,"cadberry")
print(list1)        #output:  ['cupcake', 'chocalate', 'cadberry', 'icecream', 'candy', 'cake']

#sort
list1.sort()
print(list1)        #output: ['cadberry', 'cake', 'candy', 'chocalate', 'cupcake', 'icecream']

#reverse
list1.reverse()
print(list1)         #output :['icecream', 'cupcake', 'chocalate', 'candy', 'cake', 'cadberry']
 
#clear
list1.clear()
print(list1)           #empty output: []

#count
letter = ["a","b","c","q","q","a","c","q"]
x =letter.count("a")
print(x)                # count 2 output : 2

y = letter.count("q")
print(y)                    #3
 
#extend
fruit = ["aam","kela","chiko","gam"]
fruit.extend(["strawberry","cherry"])
print(fruit)                     #extend list output: ['aam', 'kela', 'chiko', 'gam', 'strawberry', 'cherry']



