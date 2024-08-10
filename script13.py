# int as a parameter and int as a return type 
def number(a,b):
    return a + b
z=number(10,10)
print(z)

# float value as a parameter and float value as return type
def num1(a,b):
    return a * b
z1=num1(1.2,4.2)
print(z1)

# boolean value as a parameter and boolean value as a return type
def drive(age,ab):
    if age>=19 and ab:
        return True
    else:
        return False
z2=drive(5,True)
print(z2)
    
def eligible(age,na):
    if age<15 and na:
        return True
    else:
        return False
z3=eligible(22,True)
print(z3)

# string as a parameter and string as a return type
def greet(word):
    return "hello" + " Ruchi"
a=greet("hye")
print(a)

def greet1(word):
    return "hye" + " bye"
q=greet1("hye")
print(q)

# list a parameter and list a return type 
info =["ruchika","kumbhare",22]
def adde(lst):
    lst.append(123)
    return lst
a2=adde(info)
print(a2)


names = ["riya","priya","neeya"]
def add(list):
    list.append("miyaa")
    return list
a3=add(names)
print(a3)


# dict as a parameter and dict as a return type 
stud = {
    "fname":"ruchika",
    "lname":"kumbhare",
    "age":22   
}
def add1toD(info):
    info['language'] = "marathi"
    info.update({"age":21})
    return info
a4=add1toD(stud)
print(a4)
    
    
infor = {
    "fname":"virat",
    "lname":"kohli",
    "age":35,
    "number":123   
}

def inform(aaa):
    aaa['city']="banglore"
    aaa.update({'city':'mumbai'})
    return  aaa
a5=inform(infor)
print(a5)
  
# tuple as a parameter and tuple as a return type
num = (11,22,34,55)
def adde(tup):
    tup = list(tup)
    tup.append(100)
    tup=tuple(tup)
    return tup
a6=adde(num)
print(a6)
 
# set as a parameter and set as a return type 
a1 = {11,22,33,44}
print(type(a1))
def adde(ele):
    ele.add(70)
    ele.add(3000)
    return ele
a7=adde(a1)
print(a7)
