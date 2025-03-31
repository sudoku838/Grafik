import numpy as np
import matplotlib.pyplot as plt

# Создаем массив значений x от -10 до 10 с шагом 0.1
x = np.arange(-10, 10, 0.1)

# Уравнение параболы y = x^2
y = x ** 2

# Создаем график
plt.figure(figsize=(8, 6))  # Размер графика
plt.plot(x, y, label='y = x²', color='blue', linewidth=2)  # Линия параболы

# Добавляем название графика и подписи осей
plt.title('График параболы y = x²', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)

# Добавляем сетку и легенду
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

# Выделяем начало координат (0, 0)
plt.scatter(0, 0, color='red', label='Начало (0, 0)')
plt.legend()

# Показываем график
plt.show()