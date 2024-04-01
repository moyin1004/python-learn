import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt

n = 10
p = 0.4
sample_size = 15000
expected_value = n*p
N_samples = range(1, sample_size, 10)

for k in range(3):
    binom_rv = binom(n=n, p=p)
    X = binom_rv.rvs(size=sample_size)
    sample_average = [X[:i].mean() for i in N_samples]
    plt.plot(N_samples, sample_average, label='average of sample {}'.format(k))

plt.plot(N_samples, expected_value*np.ones_like(sample_average), ls='--',
        label='true expected value:n*p={}'.format(expected_value), c='k')
plt.legend()
plt.grid(ls='--')
plt.show()