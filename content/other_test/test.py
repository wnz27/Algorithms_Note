'''
a = []
b = ''
b += "123"
a.append(b)
print(a)


print(list(format(3,"b")))

for index in range(10,0,-1):
    print(index)

print("0"*0+"111111")
import math
print(math.floor(128/100))
print(str(1234))
print(type(str(1234)))

for i in range(1,22):
    print(i)


iii = [1,4,3,6,7,2]
testi = sorted(iii)
print(iii)
print(testi)
'''

# a = "9001 discuss.leetcode.com"
# print(a.split(" ",2))
# print(a)

a = [1,1,2,4,5,5]
print(a.index(max(a)))
a.pop(0)
a.pop(0)
print(a)

b = [1,2,3,4,5,6,7,8]
c = b[:5]
print(id(b), id(c))
