info = {
    "fname":"Ruchi",
    "lname":"kumbhare",
    "age":21,
    }

print(info)
print(type(info))

#retreive
print(info['fname'])
print(info['lname'])

#update 
info['lname'] = "sharma"
print(info)
info['age'] = 22
print(info)

#add
info['city']="pune"
print(info)

# how to find specfic key/ property exist in dictionary
print("lname" in info)     #true

for key in info:
    print(key)   #fname lname  age city

for key in info:
    print(key,info[key])  #fname ruchi  lname sharma  age 22   city pune


print(len(info))

"""



# how to find total number of properties in dictionary
q2 = len(vehicle)
print(q2)
"""