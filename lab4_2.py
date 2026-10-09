import math

k = float(input('Введіть значення k: ')) 
a = float(input('Введіть значення a: ')) 
b = float(input('Введіть значення b: ')) 
x = float(input('Введіть значення x: ')) 

W = (6 * k**3 - math.sin(a) + (math.cos(b)**2)) * math.sqrt(abs(b)) + (math.exp(x) / (3 * a**7))
print('W =', W)
