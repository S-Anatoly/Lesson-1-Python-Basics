from random import randint

#  1.Треугольник существует ли.

a = int(input('Введите сторону а -> '))
b = int(input('Введите сторону b -> '))
c = int(input('Введите сторону c -> '))

if a > b + c or b > a + c or c > b + a:
   print('Треугольника с такими сторонами не существует!')
elif a == b == c:
   print('Треугольник равносторонний')
elif a == b or b == c or c == a:
   print('Треугольник равнобедренный')
else:
   print('Треугольник разносторонний')

#----------------------------------------------------------------------
#  2. Простое или составное число

num = int(input('Введите число от 0 до 10000 -> '))
MAXIMUM = 100000
k = 2
flag = False
while num <= 0 or num > MAXIMUM:
    print('Неверно введено число!')
    num = int(input('Введите число заново -> '))
else:
    while k < num:
        if num % k == 0:
            flag = False
            break
        else:
            flag = True
        k += 1
if flag or num == 2:
    print('Число простое')
else:
    print('Число составное')

#-------------------------------------------
#   3.Угадать число от 0 до 1000.

number = randint(0, 1000)
limit = 10
counter = 0

while counter != limit:
    user_num = int(input('Введите число -> '))
    if user_num < number:
        print('Вы не угадали, ваше число меньше загаданного!')
    elif user_num > number:
        print('Вы не угадали, ваше число больше загаданного!')
    else:
        print(f'Поздравляю, вы угадали с {counter + 1} попытки!')
        break
    counter += 1
