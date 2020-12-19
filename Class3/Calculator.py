print('Choose the option which you are going to do. ("-", "+", "/", "*") ')
while True:
    n = input()
    if n == '0':
        break
    if n in ('-', '+', '/', '*'):
        print('Choose the numbers which you are going to...')
        m = float(input('first number:'))
        l = float(input('secong number:'))
        if n == '+':
            print(m +l)
        elif n == '-':
            print(m - l)
        elif n == '*':
            print(m*l)
        elif n == '/' and l !=0:
            print(m/l)
    else:
        print('Wrong sign!')
