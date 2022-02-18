import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(13,8))

P = lambda x: 1 + 1.46*x + 0.257*x**2 - 0.03012*x**3
Q = lambda y : 1 + 4.74*y + 0.44*y**2


x = np.linspace(-0.1,0.11,20)

plt.plot(x,P(x),color = 'red',label = "CНX  $P/Pном$")
plt.plot(x,Q(x),color = 'blue',label = "CНX  $Q/Qном$")
plt.title("Статически характеристики сумарной нагрузки")
plt.xlabel('δU%')
plt.grid()
plt.legend()
plt.show()