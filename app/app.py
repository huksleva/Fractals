import numpy as np
import matplotlib.pyplot as plt

# Размер изображения
WIDTH = 1000
HEIGHT = 1000

# Диапазон комплексной плоскости
x_min, x_max = -1.5, 1.5
y_min, y_max = -1.5, 1.5

# Максимальное количество итераций
MAX_ITER = 300

# Константа для множества Жюлиа
c = complex(-0.7, 0.27015)

# Создание массива пикселей
image = np.zeros((HEIGHT, WIDTH))

# Генерация фрактала
for x in range(WIDTH):
    for y in range(HEIGHT):

        # Преобразование координат пикселя в комплексное число
        zx = x_min + (x / WIDTH) * (x_max - x_min)
        zy = y_min + (y / HEIGHT) * (y_max - y_min)

        z = complex(zx, zy)

        iteration = 0

        # Итерационный процесс
        while abs(z) < 2 and iteration < MAX_ITER:
            z = z * z + c
            iteration += 1

        image[y, x] = iteration

# Отображение фрактала
plt.figure(figsize=(10, 10))
plt.imshow(
    image,
    cmap='inferno',
    extent=(x_min, x_max, y_min, y_max)
)

plt.title("Julia Set")
plt.xlabel("Re")
plt.ylabel("Im")

plt.colorbar(label="Iterations")

plt.show()