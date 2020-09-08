import numpy as np
import matplotlib.pyplot as plt
import os

n = 100  # количество точек на отрезке x

A = 512
x = np.linspace(-10, 10, n)  # создание "отрезка"

# описание функции f(x)
fx = -(A+47)*np.sin(np.sqrt(np.abs(x/2+(A+47))))    \
     -x*np.sin(np.sqrt(np.abs(x-(A+47))))

# создаем папку выхода
try:
    os.mkdir('results')
# если папка есть - продолжаем
except OSError:
    pass

complete_file = os.path.join('results', 'task_01_307B_Voronko_7.txt')
f = open(complete_file, 'w')

# записываем таблицу
f.write('x\tf(x)\n')
for i in range(n):
    f.write(str(round(x[i], 3))+'\t'+str(round(fx[i], 3))+"\n")
f.close()

# построение графика
plt.plot(x, fx)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.show()


