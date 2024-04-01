import numpy as np
import matplotlib.pyplot as plt

def randon_plt():
    mean = np.array([0,0])
    conv = np.array([[1,0],[0,1]])

    x,y = np.random.multivariate_normal(mean=mean, cov=conv, size=5000).T

    plt.figure(figsize=(6,6))
    plt.plot(x,y,'ro',alpha=0.2)
    plt.gca().axes.set_xlim(-4,4) # 移动坐标轴
    plt.gca().axes.set_ylim(-4,4)
    plt.grid(ls='--')
    plt.show()

def multivariate_normal():
    mean = np.array([0,0])
    conv_1 = np.array([[1,0],[0,1]])
    conv_2 = np.array([[4,0],[0,0.25]])

    x1,y1 = np.random.multivariate_normal(mean=mean, cov=conv_1, size=5000).T
    x2,y2 = np.random.multivariate_normal(mean=mean, cov=conv_2, size=5000).T

    plt.figure(figsize=(6,6))
    plt.plot(x1,y1,'ro',alpha=0.05)
    plt.plot(x2,y2,'bo',alpha=0.05)
    plt.gca().axes.set_xlim(-6,6)
    plt.gca().axes.set_ylim(-6,6)
    plt.grid(ls='--')
    plt.show()

def cov():
    fig, ax = plt.subplots(1, 2)
    mean = np.array([0,0])

    conv = np.array([[1, 0.85],
                    [0.85, 1]])

    x_1, y_1 = np.random.multivariate_normal(mean=mean, cov=conv, size=3000).T
    x_2 = x_1*100
    y_2 = y_1*100

    ax[0].plot(x_1, y_1, 'bo', alpha=0.05)
    ax[1].plot(x_2, y_2, 'bo', alpha=0.05)

    S_1 = np.vstack((x_1, y_1))
    S_2 = np.vstack((x_2, y_2))
    print(np.cov(S_1))
    print(np.cov(S_2))

    ax[0].grid(ls='--')
    ax[1].grid(ls='--')
    plt.show()

# multivariate_normal()
cov()
