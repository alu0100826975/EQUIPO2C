#!/src/bin/python
#-*- encoding: utf-8 -*-

import sys
import math
error = 0.000000001

# PRINCIPIO DE LA FUNCIÓN.

def newton(x):
  
  if(x>0):
    i=1
    while 1:
      aprox= abs(x - (math.log(x)/float(1/float(x)))) # Para que si la aproximación sea siempre positiva y se pueda aplicar e=abs(aprox-x).
      e = abs(aprox-x)
      if (e<error):
	print "La raiz de la función ln(x) es: %.10f" %aprox
	print "El valor de la función ln(x) es: %.10f" %math.log(aprox)
	print "Se ha aplicado %d veces el método de Newton." %i
	break
      i = i+1
      x=aprox
      
  elif (x<0):
    print "Los números negativos nos pertenecen al dominio de la función. "
  else:
    print "No se puede aplicar el método de Newton en el punto x=0."
    
# FINAL DE LA FUNCIÓN.

if __name__== "__main__":      

  if (len(sys.argv)==2):
    n = int(sys.argv[1])
  else:
    print "No se ha especificado el valor de partida. Tomaremos el valor por defecto."
    n=2

  newton(n)

   


