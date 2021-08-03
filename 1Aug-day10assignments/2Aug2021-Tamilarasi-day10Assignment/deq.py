import collections
x=collections.deque((1,5,6,4,9))
x.append(6)
x.appendleft(0)  #update left in list
x.pop() 
x.popleft()  #delete left in left
print(x)