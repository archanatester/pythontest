print('hello world')

list = [1,2,3]
print(list)

list.append(4)
print(list)

list.pop(1)
print(list)

list.remove(1)
print(list)

list.extend([5,6])
print(list)


print('remove duplicate list')

old_list = [1,2,3,4,1,2]
print(old_list)

new_list =[ ]
for i in old_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)