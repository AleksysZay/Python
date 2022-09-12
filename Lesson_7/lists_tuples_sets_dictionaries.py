list=[1,2,3,4,5]
list.append(6)#add
list.pop(1)#del
print(list, type(list))

tuple = (1,2,3,4,5)
print(tuple, type(tuple))

set = set()
set.add(3)
set.add(4)
set.remove(3)
print(set, type(set))

d = {}
# Adding the key value pair
d[5] = "Five"
d[10] = "Ten"
print("Dictionary", d)

# Removing key-value pair
del d[10]
print("Dictionary", d)