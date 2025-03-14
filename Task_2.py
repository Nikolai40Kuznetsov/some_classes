import matplotlib.pyplot as plt
import numpy as np
import math

class My_Circle:
    
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def draw(self):                    
        # Создаем график
        fig, ax = plt.subplots()
        plt.Circle((self.x, self.y), self.r, label="Круг")
        plt.xlabel('x')
        plt.ylabel('y')
        # Добавляем сетку
        plt.grid(True)
        plt.legend()
        # График
        plt.show()

sir = My_Circle(1, 1, 5)
sir.draw()