# import os
# reclen = 10
# size = os.path.getsize('ct.bin')
# n = int(size/reclen)
# with open('ct.bin','r+b') as f:
#     newN    = input('Please enter new name to  insert : ')
#     replace = input('please enter a name to replace : ')
#     newN    = newN + (reclen - len(newN)) * " "
#     replace = replace + (reclen -len(replace)) * " "
#     newN    = newN.encode()
#     replace = replace.encode()
# position = 0 
# found = False

# for x in range(n):
#     f.seek(position)
#     bb = f.read(reclen)
#     if bb ==replace:
#         found = True
#         break
#     else:
#         position = position + reclen

#     if found:
#         f.seek(position)
#         f.write(newN)
#         print('City successfully replaced')




import os 
reclen = 10 

size = os.path.getsize('ct.bin') # 30
n = int(size/reclen) # 3
with open('ct.bin',"r+b") as f:
    delete = input('please enter city to be deleted') 
    delete = delete + (reclen - len(delete)) * " " 
    delete = delete.encode()
    emptyrecord =b" "* reclen  
    position = 0
    found = False

    for x in range(n):
        f.seek(position)
        cr = f.read(reclen)
        if cr == delete:
            found = True
            break
        else:
            position  = position + 10

    if found:
        f.seek(position)
        f.write(emptyrecord)
        print('record deleted successfully')



count = 10
while count < 20:
    count+=1
    print(count)