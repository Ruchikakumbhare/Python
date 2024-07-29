
"""
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
    
"""
#dict

biodata = {
    "fname":"neha",
    "lname":"Kosare",
    "age":20
}

print(len(biodata))

#retrive

print(biodata['fname'])
print(biodata['lname'])

biodata['city']="pune"
print(biodata)

biodata['fname']="Avinash"
print(biodata)

for key in biodata:
    print(key)
  
Movies = {
    "hero":"ranbir",
    "heroine":"shardha",
    "city":"pune"
}
print(Movies['hero'])
#print(Movies["age"])
a=Movies.get('age')
print(a)

a1=Movies.pop('city')
print(Movies)

#Movies.popitem()
#print(Movies)

#Movies.clear()
#print(Movies)

Movies.update({"hero2":"Vinky"})
print(Movies)

Movies1 = Movies.copy()
Movies1['hero']="varun"
print(Movies1)
print(Movies)



list = ("neha","ruchi")
print(type(list))


list1 = "neha","ruchi"
print(type(list1))

