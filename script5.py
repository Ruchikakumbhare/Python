#........list methods
# 10 list methods
#.....................append(),pop(),remove(),index(),sort(),extend(),reverse(),clear(),count(),insert()


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

#22/07/24

color1 = ["red","blue","green","lemon","black"]
color2 =color1
color1[2]="white"
print(color2)
print(color1)  #['red', 'blue', 'white', 'lemon', 'black']

color2 =color1.copy()
color2[1]="purple"
print(color2)  #['red', 'purple', 'white', 'lemon', 'black']
print(color1)  # ['red', 'blue', 'white', 'lemon', 'black']


let1 = [12,23,45]
let2 = let1
let2[2]=90
print(let2)
print(let1)


let1=let2.copy()
let1[0]=100
print(let1)  #[100, 23, 90]
let2[2]=1000
print(let2)  #[12, 23, 1000]