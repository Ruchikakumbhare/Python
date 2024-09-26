import os
reclen = 10
size = os.path.getsize('ct.bin') 
n = int(size/reclen)

with open('ct.bin','rb') as f:
    ct = input('enter the city name you are searching!!! \n')
    ct = ct.encode()  
    position = 0 
    found = False
    
    for i in range (n):
        f.seek(position)
        str = f.read(10)
        if ct in str:
            found = True
        position = position + reclen
    if found : 
        print('city found in file ')
    else:
        print('city not found in file ')







 