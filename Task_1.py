import matplotlib.pyplot as plt
import numpy as np

class SquareEquation:
    
    def __init__(self, par_a, par_b, par_c):
        self.par_a = par_a
        self.par_b = par_b
        self.par_c = par_c
        # Создаем массив значений x
        self.x = x = np.linspace(-10, 10, 100)

    def func1(self):
        # Вычисляем соответствующие значения y
        y = self.par_a * self.x**2 + self.par_b * self.x + self.par_c
        return y


    def draw(self):                    
        # Создаем график
        fig, self.ax = plt.subplots()
        self.ax.plot(self.x, self.func1(), label=f'y = {self.par_a}x^2 + {self.par_b}x + {self.par_c}')

    def show(self):
        self.draw()
        # Подписи осей и заголовок
        plt.xlabel('x')
        plt.ylabel('y')
        # Добавляем сетку
        plt.grid(True)
        plt.legend()
        # График
        plt.show()

class Derivative(SquareEquation):
    
    def __init__(self, par_a, par_b, par_c):
        # Вызываем конструктор родительского класса
        super().__init__(par_a, par_b, par_c)
    
    def func2(self):
        # Вычисляем соответствующие значения производной
        y = 2 * self.par_a * self.x + self.par_b
        return y

    def draw(self):        
        # Создаем график
        super().draw()
        self.ax.plot(self.x, self.func2(), label=f"y' = {2 * self.par_a}x + {self.par_b}")
        

class Integral(SquareEquation):
    
    def __init__(self, par_a, par_b, par_c, constant=0):
        # Вызываем конструктор родительского класса
        super().__init__(par_a, par_b, par_c)
        self.constant = constant  # Константа интегрирования

    def func3(self):
        # Вычисляем соответствующие значения производной
        y = (self.par_a / 3) * self.x**3 + (self.par_b / 2) * self.x**2 + self.par_c * self.x + self.constant
        return y
    
    def draw(self):
        super().draw()
        # Создаем график
        self.ax.plot(self.x, self.func3(), label=f"∫y dx = ({self.par_a}/3)x^3 + ({self.par_b}/2)x^2 + {self.par_c}x + {self.constant}")

# Пример использования
equation = SquareEquation(1, 2, 1)
equation.show()
# Производная
derivative = Derivative(1, 2, 1)
derivative.show()

# Интеграл
integral = Integral(1, 2, 1, 0)  # Константа интегрирования = 0
integral.show()