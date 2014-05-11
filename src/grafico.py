
import matplotlib.pylab as pl
import numpy as np
from math import log

pl.figure(figsize=(8,6), dpi=80)

X = np.linspace(0, 5, 256, endpoint=True)
C =np.log(X)


pl.plot(X,C, color="green", linewidth=2.5, linestyle="-", label="Ln")
pl.legend(loc='lower right')
pl.xlim(-0.5,5.5)

pl.ylim(-4.5,2.5)
pl.title("Representacion grafica")

pl.savefig("ln.eps", dpi=72)

pl.show()