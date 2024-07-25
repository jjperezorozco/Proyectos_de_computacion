import numpy as np
import matplotlib.pyplot as plt

# Generar los valores entre 0 y 2π
x = np.linspace(0, 2 * np.pi, 1000)
# Computando sin(x) 
y = np.sin(x)

# Creando la grafica
plt.plot(x, y)
plt.title('Grafica sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.show()