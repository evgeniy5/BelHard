counter = 1
while True:
    try:
        x = float(input('введите число 1 = '))
    except:
        x = float(input('Введите вещественное число 1 = '))
    try:
        y = float(input('введите число 2 = '))
    except:
        y = float(input('Введите вещественное число 2 = '))
    try:
        z = input('введите значение или стоп ')
    except:
        z = input('введите значения + , -, *, / или стоп')

    print(f"кол-во циклов мат. операций = {counter}")
    counter += 1
    if z == '+':
        print(x + y)
    elif z == '-':
        print(x - y)
    elif z == '*':
        print(x * y)
    elif z == '/':
        print(x / y)
    elif z == 'стоп':
        break
