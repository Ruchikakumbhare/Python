# int as a parameter and int as a return type 
def num(a,b):
    return a + b
q=num(100,20)
print(q) #120

# float value as a parameter and float value as return type
def num1(x,y):
    return x + y
q1=num1(1.3,4.6)
print(q1)  #5.8999999999999995

# boolean value as a parameter and boolean value as a return type
def ele(age,val):
    if age<=20 and val:
     return True
    else : 
     return False
q2=ele(30,"val1")
print(q2)   #False

# string as a parameter and string as a return type
def adde(add):
    return "hello"+" world"
y1=adde("aff")
print(y1)  #hello world

# list a parameter and list a return type 
fruit = ["mango","apple","banana"]
def adde(f1):
    f1.append("cherry")
    return f1
x1=adde(fruit)
print(x1)   #['mango', 'apple', 'banana', 'cherry']

#.................... dict as a parameter and dict as a return type 
info = {
    "fname":"mitali",
    "lname":"mehta",
    "city":"pune"
}
def adde(info1):
    info1.update({"no":124})
    return info1
z=adde(info)
print(z)    #{'fname': 'mitali', 'lname': 'mehta', 'city': 'pune', 'no': 124}

#.................... tuple as a parameter and tuple as a return type
num1 = 20,30,40
def adde(app1):
    app1=list(app1)
    app1.append(50)
    app1=tuple(app1)
    return app1
y=adde(num1)
print(y)              #{1000, 10, 20, 30}
 
#................... set as a parameter and set as a return type 
num = {10,20,30}
def adde(app):
    app.add(1000)
    return app
x=adde(num)
print(x)                 #{1000, 10, 20, 30}
