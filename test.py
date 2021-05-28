from ds.stack import Stack


s1 = Stack(2)
print(s1.length())
s1.push(125)
s1.printstack()
s1.push(236)
s1.printstack()
s1.push(33)
print(s1.isEmpty())
print(s1.isFull())