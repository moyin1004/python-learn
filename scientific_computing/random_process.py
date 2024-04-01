import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
import math

def bet():
    sample_list = []
    person_num = 100000
    round_num = 10000

    for person in range(1, person_num+1):
        money = 10
        for round in range(1, round_num+1):
            result = random.randint(0,1)
            if result == 1:
                money = money+1
            elif result == 0:
                money -= 1
            if money == 0:
                break
        sample_list.append([person, round, money])

    sample_df = pd.DataFrame(sample_list, columns=['person', 'round', 'money'])
    sample_df.set_index('person', inplace=True)
    print('总轮数:{}, 总人数:{}'.format(round_num, person_num))
    print('输光的人数:{}'.format(person_num-len(sample_df[sample_df['round']==round_num])))
    print('盈利:{}'.format(len(sample_df[sample_df['money']>10])))
    print('亏损:{}'.format(len(sample_df[(sample_df['money']<=10)&(sample_df['money']>0)])))

def stock():
    s0 = 10.0 # 股价
    T = 1.0
    n = 244*T
    mu = 0.15
    sigma = 0.2 # 股价波动率
    n_simulation = 10000
    dt = T/n
    s_array = []

    for i in range(n_simulation):
        s = s0
        for j in range(int(n)):
            e = np.random.normal()
            s = s+mu*s*dt + sigma*s*e*math.sqrt(dt)
        s_array.append(s)
    print(s_array)
    plt.hist(s_array, alpha=0.6, bins=30, density=True, edgecolor='k')
    plt.grid(ls='--')
    plt.show()

def stock_change():
    s0 = 10.0 # 股价
    T = 1.0
    n = 244*T
    mu = 0.15
    sigma = 0.2 # 股价波动率
    n_simulation = 10
    dt = T/n
    random_series = np.zeros(int(n), dtype=float)
    x = range(0, int(n))

    for i in range(n_simulation):
        random_series[0] = s0
        for j in range(1, int(n)):
            e = np.random.normal()
            s = random_series[j-1]
            random_series[j] = s+mu*s*dt + sigma*s*e*math.sqrt(dt)
        plt.plot(x, random_series)
    plt.grid(ls='--')
    plt.show()

# stock()
stock_change()