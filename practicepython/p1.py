
#....................List method Practice.......................
color = ['blue','green','pink','black','black']
color.append('black')
print(color)
color.pop()
print(color)
color.remove('blue')
print(color)
color.extend(['purple','red'])
print(color)
color.sort()
print(color)
color.reverse()
print(color)
color1=color.copy()
color1[3]="peach"
print(color1)
a =color.count('black')
print(a)
a2=color.index("green")
print(a2)
color.clear()
print(color)
