
#---------- program1 checking current directory
import os
x=os.getcwd()
print(x)      #C:\Users\Rohit\Desktop\python


#--------- program2  changing the folder
# import os
# os.chdir('python/regularexp')
# print(os.getcwd())

#------- program 3 creating and removing the libraries

# os.mkdir('module2')
# os.makedirs('')
#os.makedirs('evening3/evening3b',exist_ok=True) #nested folder 

items = os.listdir('.')
print(items)