while True:
    print('Enter two words <3')
    m = input()
    m = m.split(' ')
    print(m[1], m[0])
    print('Write "0" to stop')
    n = input()
    if n == '0':
        break
