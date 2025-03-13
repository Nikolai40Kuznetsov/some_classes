import matplotlib.pyplot as plt
import numpy as np

class SquareEquation:
    
    def __init__(self, par_a, par_b, par_c):
        self.par_a = par_a
        self.par_b = par_b
        self.par_c = par_c
        
    def draw(self):
        # Создаем массив значений x
        x = np.linspace(-10, 10, 100)
        
        # Вычисляем соответствующие значения y
        y = self.par_a * x**2 + self.par_b * x + self.par_c
        
        # Создаем график
        plt.plot(x, y, label=f'y = {self.par_a}x^2 + {self.par_b}x + {self.par_c}')
        
        # Подписи осей и заголовок
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('График квадратного уравнения')
        
        # Добавляем сетку
        plt.grid(True)
        
        plt.legend()
        
        # График
        plt.show()

class Derivative(SquareEquation):
    
    def __init__(self, par_a, par_b, par_c):
        # Вызываем конструктор родительского класса
        super().__init__(par_a, par_b, par_c)
    
    def calculate(self, x):
        return 2 * self.par_a * x + self.par_b
    
    def draw(self):
        # Создаем массив значений x
        x = np.linspace(-10, 10, 100)
        
        # Вычисляем соответствующие значения производной
        y = self.calculate(x)
        
        # Создаем график
        plt.plot(x, y, label=f"y' = {2 * self.par_a}x + {self.par_b}")
        
        # Добавляем подписи осей и заголовок
        plt.xlabel('x')
        plt.ylabel("y'")
        plt.title('График производной квадратного уравнения')
        
        # Добавляем сетку
        plt.grid(True)
        
        # Добавляем легенду
        plt.legend()
        
        # Показываем график
        plt.show()

class Integral(SquareEquation):
    
    def __init__(self, par_a, par_b, par_c, constant=0):
        # Вызываем конструктор родительского класса
        super().__init__(par_a, par_b, par_c)
        self.constant = constant  # Константа интегрирования
    
    def calculate(self, x):
        # Интеграл квадратного уравнения: (a/3)x^3 + (b/2)x^2 + cx + d
        return (self.par_a / 3) * x**3 + (self.par_b / 2) * x**2 + self.par_c * x + self.constant
    
    def draw(self):
        # Создаем массив значений x
        x = np.linspace(-10, 10, 100)
        
        # Вычисляем соответствующие значения интеграла
        y = self.calculate(x)
        
        # Создаем график
        plt.plot(x, y, label=f"∫y dx = ({self.par_a}/3)x³ + ({self.par_b}/2)x² + {self.par_c}x + {self.constant}")
        
        # Добавляем подписи осей и заголовок
        plt.xlabel('x')
        plt.ylabel('∫y dx')
        plt.title('График интеграла квадратного уравнения')
        
        # Добавляем сетку
        plt.grid(True)
        
        # Добавляем легенду
        plt.legend()
        
        # Показываем график
        plt.show()

# Пример использования
equation = SquareEquation(1, 2, 1)
equation.draw()

# Производная
derivative = Derivative(1, 2, 1)
derivative.draw()

# Интеграл
integral = Integral(1, 2, 1, 0)  # Константа интегрирования = 0
integral.draw()