# python3.10.11
from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np
import math


def float_compare(x, y) -> bool:
    return x-y < 1e-8 and x-y > -1e-8

def binom_plot():
    _, ax = plt.subplots(3, 1)
    params = [(10,0.25),(10,0.5),(10,0.8)]
    x = range(0,11)
    for i in range(len(params)):
        binom_rv = binom(n=params[i][0], p=params[i][1])
        y = binom_rv.pmf(x)
        print(y[10], math.isclose(params[i][1]**10, y[10]))
        ax[i].set_title('n={},p={}'.format(params[i][0],params[i][1]))
        ax[i].plot(x, y, 'bo', ms=8)
        ax[i].vlines(x, 0, y, colors='b', lw=3)
        ax[i].set_xlim(0,10)
        ax[i].set_ylim(0,0.35)
        ax[i].set_xticks(x)
        ax[i].set_yticks([0,0.1,0.2,0.3])
        ax[i].grid(ls='--')
    plt.show()

def sampling():
    _, ax = plt.subplots(3, 1)
    params = [(10,0.25),(10,0.5),(10,0.8)]
    x = range(0,11)
    for i in range(len(params)):
        binom_rv = binom(n=params[i][0], p=params[i][1])
        rvs = binom_rv.rvs(size=10000)
        print(rvs)
        ax[i].hist(rvs, bins=11, density=True, alpha=0.6, edgecolor='k')
        ax[i].set_title('n={},p={}'.format(params[i][0],params[i][1]))
        ax[i].set_xlim(0,10)
        ax[i].set_ylim(0,0.4)
        ax[i].set_xticks(x)
        ax[i].set_yticks([0,0.1,0.2,0.3,0.4])
        ax[i].grid(ls='--')
        print('rvs{}:{}'.format(i,rvs))
    plt.show()

def digital_features():
    binom_rv = binom(n=10, p=0.25)
    mean, var, skew, kurt = binom_rv.stats(moments='mvsk')
    rvs = binom_rv.rvs(size=10000)
    E_sam = np.mean(rvs)
    S_sam = np.std(rvs)
    V_sam = S_sam ** 2
    print("mean:{},var:{}".format(mean, var))
    print("E_sam={},V_sam={}".format(E_sam,V_sam))
    print("E=np={},V=np(1-p)={}".format(10*0.25,10*0.25*0.75))

if __name__ == "__main__":
    sampling()
    # digital_features()