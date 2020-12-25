z = open('data.txt', 'w')

z.write('Enter the phrase <3' + '\n')
c = input()
z.write(c + '\n')

z.write('How many time do u want your phrase to be displayed?' + '\n')
x = int(input())

for i in range(0, x):
    z.write(c +  '\n')
z.close()
