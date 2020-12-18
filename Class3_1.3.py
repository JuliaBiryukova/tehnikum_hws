print('Enter the price for 1 kilo of asphalt;)')
while True:
    m = input()
    print(m[::-1])
    print('Want to add a new price?')
    n = input()
    if n == 'yes':
        print('Enter the next price')
        l = input()
        print(l[::-1])
    if n == 'no':
        print('Thanks <3')
        break
