food = {
    "soup" : "manchau",
    "fruit": "mango",
    "Dish": "Dosa",
    "drink":"Fruity",
    "icecream":"chocochips"
}

print(len(food))   #5

#methods of dic  
a = food.get("soup")
print(a)          #manchau

food.pop("Dish")
print(food)        #  {'soup': 'manchau', 'fruit': 'mango', 'drink': 'Fruity', 'icecream': 'chocochips'}
 
food.popitem()      
print(food)         #last ele dlt krenga      {'soup': 'manchau', 'fruit': 'mango', 'drink': 'Fruity'}

food.update({'waffers':"chips"})
print(food)

food1 = food.copy()
food1['dish'] = "dosa"
print(food1)      #{'soup': 'manchau', 'fruit': 'mango', 'drink': 'Fruity', 'waffers': 'chips', 'dish': 'dosa'}
print(food)      #{'soup': 'manchau', 'fruit': 'mango', 'drink': 'Fruity', 'waffers': 'chips'}

food1.clear()
print(food1)         #{}



movies = {
    "hero":"ranbir",
    "heroine":"shardha",
    "city":"pune"
}

for x in movies.keys():
    print(x)
    
for x in movies.values():
    print(x)
    
for x in movies.items():
    print(x)
    
food = {
    "soup" : "manchau",
    "fruit": "mango",
    "Dish": "Dosa",
    "drink":"Fruity",
    "icecream":"chocochips"
}
print("drink"[0])