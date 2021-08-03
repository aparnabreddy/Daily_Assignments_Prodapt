#deque doubly ended que

# import collections
# x=collections.deque([1,2,3,4,5])
# x.append(6)
# x.appendleft(0)
# print(x)
# x.pop()
# x.popleft()
# print(x)


#chainmaps

import collections
d1={"name":"kalai","age":22}
d2={"name":"abi","age":22}
comdic=collections.ChainMap(d1,d2)
print(comdic.maps)
print(list(comdic.values()))
print(list(comdic.keys()))

