import collections
names=[]
for i in range(10):
    name=input("Enter the name:")
    names.append(name)
c=collections.Counter(names)
print(c)