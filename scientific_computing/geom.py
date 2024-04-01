# python3.10.11
from scipy.stats import geom
import matplotlib.pyplot as plt

fig, ax = plt.subplots(2,1)
params = [0.5,0.25]
x = range(1,11)

for i in range(len(params)):
    geom_rv = geom(p=params[i])
    ax[i].set_title('p={}'.format(params[i]))
    y = geom_rv.pmf(x)
    ax[i].plot(x, y, 'bo', ms=8)
    ax[i].vlines(x, 0, y, colors='b', lw=5)
    ax[i].set_xlim(0,10)
    ax[i].set_ylim(0,0.6)
    ax[i].set_xticks(x)
    ax[i].set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6])
    ax[i].grid(ls='--')
plt.show()