# 1. Напишите функцию для транспонирования матрицы
listt = [[11, 42, 31], [56, 15, 95], [14, 35, 64]]

# создаем список
l = [[0 for i in range(len(listt))] for j in range(len(listt[0]))]

# заполняем новый список значениями из старого с транспонированием
for i in range(len(listt)):
    for j in range(len(listt[0])):
        l[i][j] = listt[j][i]

# Вывод старого списка
for i in range(len(listt)):
    print(listt[i])
print()

# Вывод нового списка
for i in range(len(l)):
    print(l[i])

# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


# 3. Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

summ = 0.0  # сумма на счету
count = 0  # количество операций
log = []  # список для записи операций


# Пополнить
def top_up(money):
    global summ, count
    # если на счету больше 5млн то списывается 10%
    if summ > 5_000_000:
        summ -= (summ / 100) * 10
        log.append(f'Вычтено 10%')

    summ += money
    count += 1
    log.append(f'Поступление {money}')
    if count == 3:
        summ += summ / 100 * 3
        log.append(f'Начислено 3%')
        count = 0
    print(f'Баланс -> {summ}')


# процент за снятие 1,5  но не меньше 30 и не больше 600уе
def take_off(money):
    global summ, count

    if summ > 5_000_000:
        summ -= (summ / 100) * 10
        log.append(f'Вычтено 10%')

    if money > summ:
        print('Недостаточно средств!')
        log.append(f'Попытка списать {money}, но недостаточно')
        count += 1
        if count == 3:
            summ += summ / 100 * 3
            log.append(f'Начислено 3%')
            count = 0
    else:
        summ -= money
        proc = (money / 100) * 1.5
        if proc < money:
            summ -= 30
        elif proc > 600:
            summ -= 600
        else:
            summ -= proc
        count += 1

        if count == 3:
            summ += summ / 100 * 3
            log.append(f'Начислено 3%')
            count = 0
        log.append(f'Снятие {money}')
    print(f'Баланс -> {summ}')


# Выйти
def exit_b():
    global count

    if summ > 5_000_000:
        summ -= (summ / 100) * 10
        log.append(f'Вычтено 10%')

    print('Заберите карту!')
    log.append('Выход')
    count += 1

    if count == 3:
        summ += summ / 100 * 3
        log.append(f'Начислено 3%')
        count = 0
    exit()

# Проверка работы
top_up(1000.0)
take_off(100.0)
top_up(6000000.0)
take_off(100.0)
take_off(10000000.0)
top_up(10000000.0)
take_off(56790.0)
print(log)
exit_b()
