# python3.10.11
from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np

lambda_ = 2
data = poisson.rvs(mu=lambda_, size=100000)
plt.figure()
plt.hist(data, density=True, alpha=0.6, edgecolor='k')
plt.gca().axes.set_xticks(range(0,11))
print('mean={}'.format(np.mean(data)))
print('var={}'.format(np.square(np.std(data))))
plt.grid(ls='--')
plt.show()