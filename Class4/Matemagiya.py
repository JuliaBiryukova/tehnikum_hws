while True:
    
    print('Choose the number:')
    n = int(input())
    x = 0
    for i in range(1, n + 1):
        
        x += i
    b = n* (n + 1)//2
    print(x)
    print(b)
