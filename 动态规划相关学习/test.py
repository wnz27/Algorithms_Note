a = "abcde12345"
b = 2*a
print(b)
n = 3
count = 0
while n != 1:
    if n % 2 == 0:
        n = n/2
        count += 1
    else:
        n = (3*n+1) / 2
        count += 1
print(count)

print(10000 and 100)