print('Write the list of numbers')
z = []
while len(z) != 8:
    x = int(input('enter the number:'))
    x = z.append(x)
    print(z)
print('write the index of the number which you wnat to remove:')
c = int(input())
print(z[c:c + 1])
c = z.remove(c)
print(z.pop())
print(z)
