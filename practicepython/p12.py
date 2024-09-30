# a = int(input('enter a number : '))
# b = int(input('enter a second number : '))
# c = a/b
# print(c)


# try:
#     a = int(input('enter a number : '))
#     b = int(input('enter a second number : '))
#     print(a/b)
# except:
#     print('error error')

# try:
#     a = int(input('enter a number : '))
#     b = int(input('enter a second number : '))
#     print(a/b)
# except ZeroDivisionError:
#     print('value is not devided by zero')
# except ValueError:
#     print('value is not proper')
# except TypeError:
#     print('type error is occured')
# except:
#     print('Errorrrrr')

# try:
#     no = [2,3,45,5]
#     a = int(input('enter a index number : '))
#     print(no[a])
# except IndexError:
#     print('index is not found')
# except:
#     print('error')
# finally:
#     print('executed')

try:
    x = 10/0
except ZeroDivisionError:
    print('error')


# print('hiee')
# try:
#     x = 1/0
# except ZeroDivisionError:
#     print("you can't divide by zero")
# print('Bye')
