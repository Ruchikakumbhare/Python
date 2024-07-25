#dictonary 24/07

"""
data = {
    "vegitable" : "Potato",
    "color" : "orange",
    "buscuit": "Monaco",
}

#print(type(data))
#print(data)

print(data['color'])   #retreive
print(data.get('color'))  #.get           #orange    
print(data.get('city'))                    #agr dic main koi element nhi raha to none return krta hai
"""




student = {
    "fname":"shiwit",
    "lname":"tomar",
    "age":28,
    "contact":123,
}

#get()
print(student.get("age"))             #28
print(student.get("number"))          #none

#clear()
#student.clear()
#print(student)                      #{}

#copy()
student1=student.copy()
student1['age'] = 25
print(student)          #{'fname': 'shiwit', 'lname': 'tomar', 'age': 28, 'contact': 123}
print(student1)         #{'fname': 'shiwit', 'lname': 'tomar', 'age': 25, 'contact': 123}

#pop
student.pop("contact")
print(student)            #{'fname': 'shiwit', 'lname': 'tomar', 'age': 28}

#popitem
student.popitem()
print(student)              #{'fname': 'shiwit', 'lname': 'tomar'} last item is remove

#update
student.update({'city' : "mumbai"})
print(student)                # {'fname': 'shiwit', 'lname': 'tomar', 'city': 'mumbai'}

student1 = {
    "fname" : "Anika",
    "lname" : "Thapar",
    "age" :25,
}
for x in student1.values():
    print(x)
    
for x in student1.keys():
    print(x)
    
for x in student1.items():
    print(x)