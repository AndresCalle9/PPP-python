import numpy as np
import math as m
import matplotlib.pyplot as plt

# Nuevas caracteristicas para PPP
# Cómo no sé bien como se llaman las señales originales que se van a usar las voy a identificar así
# Freq : Vector del eje "x" en el barrido de frecuencias (fourier)
# Amp : Vector del eje "y" en el barrido de frecuencias (fourier)
# Amp0 : valor de amplitud de la señal suministrada al tejido por el transductor
# No encontré carácteristicas ligadas a la fase

Freq = np.arange(start=0, stop=1000, step=1)
Amp = np.random.random(1000)
Amp0 = 1.0

# Generar un vector de potencias para evaluar las señales 20*log(vout/vin)
Power = []
for i in range(len(Freq)):
    aux = 20 * m.log10(Amp[i]/Amp0)
    Power.append(abs(aux))

# Potencia máxima de la señal (C1)
max_pow = max(Power)
max_index: int = Power.index(max_pow)
# Frecuencia en donde se obtuvo esta potencia máxima(C2)
freq_max = Freq.item(max_index)

# Potencia promedio de la señal (C3)
mean_pow = np.mean(Power)

# Pendiente positiva del espectro (C4) e intercepto en y (C5)
x = Freq[0: max_index]
y = Power[0: max_index]
x_mean = np.mean(x)
y_mean = np.mean(y)
n = len(x)
num = 0.0
den = 0.0
for i in range(n):
    num += ((x[i] - x_mean) * (y[i] - y_mean))
    den += ((x[i] - x_mean) ** 2)
m = num/den
b = y_mean - (m - x_mean)

# Pendiente negativa del espectro (C6) e intercepto en y (C7)
x = Freq[max_index: len(Freq)]
y = Power[max_index: len(Power)]
x_mean = np.mean(x)
y_mean = np.mean(y)
n = len(x)
num = 0.0
den = 0.0
for i in range(n):
    num += ((x[i] - x_mean) * (y[i] - y_mean))
    den += ((x[i] - x_mean) ** 2)
m = num/den
b = y_mean - (m - x_mean)

# Despues de probar estas caracteristicas efectuar el clasificador con solo con una caracteriticas y almacenar el score
# obtendo en cada uno


# Selecionar las caracteristicas que den el mejor score


# Realizar una PCA con estas "mejores caracteristicas"


# Probar K-fold con este proceso a ver si se logra un mejor accuracy

