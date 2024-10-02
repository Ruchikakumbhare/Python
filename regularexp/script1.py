# regular Expression `s methods:
# search
# findall
# match
# split
# sub

#--------------- program1 (search)
# import re
# str = 'hi hello how you'
# obj=re.search(r'h\w\w',str)       # r--> Raw string   \w --> [a-z ,A-Z ,0-9]
# print(obj)                       # o/p--> <re.Match object; span=(3, 6), match='hel'>  
# print(obj.group())   #hel

# import re
# str1 = 'cat dog hen peacock'
# obj =re.search(r'd\w\w',str1)
# print(obj.group())

# import re
# str1 = 'cat dog hen peacock'
# result =re.search(r'd\w\w',str1)
# if(result): 
#      print(result.group())

#-----------------program 2 (findall)
import re
str2 = 'hello i am good girl '
x=re.findall(r'g\w\w',str2)
print(x)                   #['goo', 'gir'] find all g   

str2 = "hello i am good girl"
listA = re.findall(r'g\w\w\w',str2)
print(listA)       #['good' , 'girl']

#------------------program 3 (match) (start main match hua to hi o/p aynga)
str3 = 'see you soon'
x=re.match(r's\w',str3)
print(x)
print(x.group())    #see   

str4 = 'python is easy language'
y=re.match(r'e\w\w',str4)
print(y)             #None

str4 = 'python is easy language'
y=re.search(r'e\w\w',str4)
print(y)             #eas       beacuase of search method


#------------------program 4 (split)
#not [a-z A-Z 0-9]
str5 = "This ; is the : 'Core' python's book"
x1=re.split(r'\W+',str5)        #capital W
print(x1)                

str5 = "ruchi-749-@gmail"
x2 = re.split(r'\W+',str5)
print(x2)


#------------------- program 5(sub)
str6 = "I am learning javascript"
f5 = re.sub(r'javascript','python',str6)
print(f5)

str7 = ' i am bad girl'
y1=re.sub(r'bad','good',str7)
print(y1)