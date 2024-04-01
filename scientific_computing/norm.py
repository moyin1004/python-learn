# python3.10.11
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1,1)
norm_0 = norm(loc=0,scale=1)
norm_1 = norm(loc=1,scale=2)

x = np.linspace(-10, 10, 1000)
y = norm_0.pdf(x)
ax.plot(x, y,  color='red', lw=3, alpha=0.6, label='loc=0,scale=1')
y = norm_1.pdf(x)
ax.plot(x, y,  color='blue', lw=3, alpha=0.6, label='loc=1,scale=2')
ax.legend(loc='best')
ax.grid(ls='--')
plt.show()