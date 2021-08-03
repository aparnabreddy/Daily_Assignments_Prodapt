# # DefaultDict
# import collections
# x=collections.defaultdict(str)
# x["name"]="Priya"
# x["Rollno"]="106"
# print(x["Admnoo"])


# OrderedDict
# import collections
# d1=collections.OrderedDict()
# d1['name'] = "Annop"
# d1['rollno'] = "22"
# d1['admno'] = "1005"
# # print(d1)
# for key,value in d1.items():
#     print(key,value)

# # counter
# import collections
# x=collections.Counter(["Hello","Hello","Hai"])
# print(x)

# import collections
# x=collections.defaultdict(str)
# x["name"]="Rahul"
# x["Rollno"]="105"
# print(x)
# print(x["Admnoo"])

# from typing import ChainMap, DefaultDict, Deque


# Deque - Doubly Ended queue
# import collections
# x=collections.deque([1,2,3,4,5])
# # x.append(6)
# # x.appendleft(0)
# x.pop()
# x.popleft()
# print(x)

# # ChainMap
# import collections
# dict1={"name":"Vaishnavi","Age":21}
# dict2={"name":"Priya","Age":21}
# comb_dict=collections.ChainMap(dict1,dict2)
# print(comb_dict.maps)
# print(list(comb_dict.values()))