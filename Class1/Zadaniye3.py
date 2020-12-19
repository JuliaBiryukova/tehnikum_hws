a = int(input())
b = int(input())
print('now, choose the option which you are going to do,"-","+", "*", "/" ')
c=input()
options=['-', '+', '*', '/']
while c in options:
    if c =='0':
        break
    if c == '+':
        print(a+b)
    if c == '-':
        print(a-b)
    if c == '*':
        print(a*b)
    if c == '/' and b != 0:
        print(a/b)
else:
 print('invalid operation sing')
