
# # #*
# # a an ann
# # #a[\w]* 
# #[\w] --> [A-Z a-z 0-9]
# # \b - blank space
# # \d -  digit ---> 0 ,1 , 2, 3,4,5,6,7,8,9

# program1
import re
str = "this is an apple and please eat!!"
a=re.findall(r'a[\w]*' , str)     #[\w]*--> more than 
print(a)                          #['an', 'apple', 'and', 'ase', 'at']


# program2
import re
str1 = "this is an apple and please eat!!"
a2=re.findall(r'le[\w]*',str1)
print(a2)  #['le', 'lease']

# program3
str3 = "The meeting will be conducted on 1st and 21st of every month"
a3=re.findall(r'\d[\w]*',str3)
print(a3)       #['1st', '21st']


# program4
a3=re.findall(r'\d[\d]*',str3)
print(a3)        #['1', '21']

# program5
str = 'seven two three four ten'
a4=re.findall(r'\b\w{3}\b',str)
print(a4)         #['two', 'ten']


a5=re.findall(r'\b\w{5}\b',str)
print(a5)        #['seven', 'three']

# program6
a6 =re.findall(r'\b\w{3,}',str)
print(a6)          #more than 3 
 
# program7
a7=re.findall(r'\b\w{3,4}',str)
print(a7)         #['seve', 'two', 'thre', 'four', 'ten']

a8=re.findall(r'\b\d{1,}\b',str)
print(a8)

#program 8
str8 = "one two three four five six 7 8 9 10"
str8  = re.findall(r'\b\d{1,}\b',str8)
print(str8)







