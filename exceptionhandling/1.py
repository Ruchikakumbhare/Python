#------------------------------------------------------ program1----------------------------------------------------------
# print('welcome')
# a = int(input('enter a number....\n'))
# b = int(input('enter a number....\n'))
# print(a/b)
# print('executed')


#------------------------------------------------------ program2----------------------------------------------------------
# print('welcome welcome!!')
# try:
#      a = int(input('enter a number....\n'))
#      b = int(input('enter a number....\n'))
#      print(a/b)
# except:
#     print('error occured')
   
# print('see you again')


#------------------------------------------------------ program3----------------------------------------------------------

# print('welcome welcome!!')
# try:
#      a = int(input('enter a number....\n'))
#      b = int(input('enter a number....\n'))
#      print(a/b)
     
# except ZeroDivisionError:
#     print('please enter correct input')  #10/0

# except ValueError:
#     print('please enter correct value')  #10f

# except:
#     print('please enter valid input')

# print('bye bye')


#------------------------------------------------------ program4----------------------------------------------------------
 
# try:
#     num = [10,20,30,40]
#     a = int(input('enter the index : '))
#     print(num[a])
# except IndexError:
#     print('please correct the index number')
# finally:
#     print('i will always execute') 
 
 
#-----------------------------------------------------------------------------------------------------------------------------
# try  except else finally
# Basic try - except block

# -------------------program 1
# print('hiee')
# try:
#     x = 1/0
# except ZeroDivisionError:
#     print("you can't divide by zero")
# print('Bye')


#---------------------program 2
# try:
#     a = int(input('enter a number : '))
#     b = int(input('enter a number : '))
#     print(a/b)
# except ZeroDivisionError:
#     print('cannot divisible by zero')
# except ValueError:
#     print('A value error occured')
# except Exception as e:
#     print('any exception not know')
    

#---------------------- program 3 
# Generic way of raising exception 
# try:
#     num = [10,20,30]
#     a = int(input('enter a number : '))
#     b = int(input('enter a number : '))
#     print(a/b)
#     print(num[3])
# except ValueError:
#     print("A value error occured")
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except Exception as e:
#     print("any exception not known")
#     print(e)



#----------------------- program 4
# try except else 
# try:
#     x = int(10)
#     print('heloo')
# except ValueError:
#     print(' a value error occured')
# except Exception as e:
#     print(e)
# else:
#     print('i will run if no exception is raised')
    
# try:
#     x = int('a')
#     print("hello")
# except ValueError:
#     print("A value error occured")
# except Exception as e:
#     print(e)
# else:
#     print("i will run if no exception is raised")



#-------------------------------program 5
# try except else finally

# try :
#     x = 1/0
# except ZeroDivisionError:
#      print("you cannot divide by zero..")
# else:
#     print('no exception raiseed')    
# finally:
#     print('i am always excute')
# # ----------
# try :
#     x = 1/4
# except ZeroDivisionError:
#      print("you cannot divide by zero..")
# else:
#     print('no exception raiseed')    
# finally:
#     print('i am always excute')

# finally block always execute irrespective of 
# exception raised or no exception raised

#-------------------------------program 6
#  Raising the exception manually

# def check_age(age):
#     if age <=18:
#         raise ValueError('age must be greater than 18')
#     return True

# try:
#     check_age(10)
#     print('success')
# except ValueError as e:
#     print(e)

#-------------------------------program 7
# Exception --
# customised
class underA(Exception):
    pass
def check_age(age):
    if age <=18:
        raise ValueError('age must be greater than 18')
    return True

try:
    check_age(19)
    print('success')
except ValueError as e:
    print(e)


#-------------------------------program 8
# assert 
def checkP(x):
    assert x > 0 , 'x must be positive'

try:
    checkP(10)
    print('+ve number')
except AssertionError as e:
    print(e)
#--------- 
def checkP(x):
    assert x > 0 , 'x must be positive'

try:
    checkP(-10)
    print('+ve number')
except AssertionError as e:
    print(e)    
    
#-------------------------------- program 9
try:
    with open('f1.txt','rb') as f:
       x = f.read()
       print(x)
except FileNotFoundError:
    print('file not found')

# try:
#     with open('filetext2.txt',"r+") as f:
#         c = f.read()
#         print(c)
# except FileNotFoundError:
#     print("File not found")

# # finally:
# #     f.close()


# # Keyerror exception