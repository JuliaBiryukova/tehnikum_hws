import random, time
c = 0
print('Хей, сыграем в игру? Я загадываю любое число, а ты должен его отгадать:)')
n = random.randint(0,100)
print('Ну всё, загадал')
while True:
     print('Ваш ответ: ')
     c = int(input())
     if c > n:
          print('Моё число меньше ')
     if c < n:
          print('Моё число больше! ')
     if (c == n+1) or (c == n-1):
          print('Горячо!')
     elif (c == n+2) or (c == n-2):
          print('Теплее')
     elif a == n:
          break
time.sleep(2)
print('Ну что ж... Молодец')
