import math

x = float(input("Введіть x: "))

if x > 0:
    if math.sqrt(5*x) + math.log2(abs(x + 4)) !=0:
        f = (math.sin(x + 4) - math.cos(3 * x)) / (math.sqrt(5*x) + math.log2(abs(x + 4)))
        print('f(x) =', f)
    else:
        print('Помилка: Знаменник дорівнює нулю')
else:
    print('Функція не визначена для цього x.')