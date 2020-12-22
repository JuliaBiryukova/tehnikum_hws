print('enter 3 numbers to find out which one is the average')
a = int(input('first number:'))
b = int(input('second number:'))
c = int(input('third number:'))
if a<b<c or c<b<a:
    print (b)
elif b<c<a or a<c<b:
    print(c)
elif b<a<c or c<a<b:
    print(a)
