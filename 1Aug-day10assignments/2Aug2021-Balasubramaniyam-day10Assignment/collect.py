import collections
# from typing import Counter
# employee=collections.namedtuple("employee",["name","empid","salary"])
# e=employee("balu","1000","20000")
# print(e.name)

# # import collections


# d=collections.OrderedDict()
# d['name']="Balu"
# d['id']="1000"
# d['salary']="20000"
# for key,value in d.items():
#     print(key,value)

# c=collections.Counter(["Hello","Hello","Hello","hai"])
# print(c)
# names=[]
# for i in range(10):
#     name=input("enter names :")
#     names.append(name)
# c=collections.Counter(names)
# print(c)

# default Dictionary
# def values():
#     return "Key is Not present"
# dictionary=collections.defaultdict(values)
# dictionary["name"]="balu"
# dictionary["roll"]="22"
# print(dictionary["salary"])

#deque
# de=collections.deque([1,2,3,4,5])
# de.append(6)
# print(de)
# de.appendleft(0)
# print(de)
# de.pop()
# print(de)
# de.popleft()
# print(de)

# ChainMap
dict1={"name":"Robert" ,"age":"22"}
dict2={"name":"Balu" ,"age":"21"}
chain={}
if len(chain)==0:
    chain=collections.ChainMap(dict1)
chain=chain.new_child(dict2)
print(chain)