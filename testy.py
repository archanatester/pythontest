import array as arr

x=arr.array('I',[1,2,3])
x.append(4)
print(x)

x.extend([5,6])
print(x)

x.insert(2,7)
print(x)

x.pop()
print(x)

x.pop(2)
print(x)

x.remove(4)
print(x)


list = [2,4,1,3,0]
list.sort()
print(list)

y=[5,3,1]
z=list(reverse(y))
print(z)