

color = {'blue','red','brown','pink','orange'}
print(type(color))
print(color)
print(len(color))
print('orange' in color)

for x in color:
    print(x)
    
color.add('black')
print(color)

color1=color.copy()
color1.add('white')
print(color1)

color.pop()
print(color)

color.remove('pink')
print(color)

color1.clear()
print(color1)

color.update({'skin','yellow','purple'})
print(color)