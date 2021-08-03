import collections as c
employees=c.namedtuple("employees",["name","emid","salary"])
e1=employees("kalai","101","25000")
print(e1.name)
print(e1[1])