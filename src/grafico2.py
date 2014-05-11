
import matplotlib.pylab as pl
import numpy as np
from math import log

# Lista con los valores de partida
x = [1, 2, 3,  4, 5, 6, 6.5, 7, 7.35, ]

# Lista con los valores de l tiempo
y = [0.1154410839, 0.5907168388,  0.6773560047, 0.5563027859, 0.7719118595, 0.9161560535, 0.8663120270, 0.9962458611, 1.3717629910]

# Utilizar la funcion plot para trazar el grafico
pl.plot(x,y, color="green", linewidth=2.5, linestyle="-")

# Incluir un titulo
pl.title('Valor inicial frente a tiempo CPU por 100000 ejecuciones')

# Poner etiquetas en los ejes
pl.xlabel('Valor inicial')
pl.ylabel('Tiempo de CPU')

# Poner limites a los ejes
pl.xlim(0.0, 8)
pl.ylim(0.0, 1.7)

# mostrar por la consola el resultado
pl.savefig("time.eps", dpi=72)
pl.show()



