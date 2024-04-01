import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from scipy.stats import uniform

n = 100000
r = 1.0
ox, oy = (0., 0.)

uniform_x = uniform(ox-r, 2*r).rvs(n)
uniform_y = uniform(oy-r, 2*r).rvs(n)

d_array = np.sqrt((uniform_x-ox)**2+(uniform_y)**2)

res = sum(np.where(d_array < r, 1, 0))
pi = (res/n)/(r**2)*(2*r)**2

fig,ax = plt.subplots(1,1)
plt.plot(uniform_x, uniform_y, 'ro', alpha=0.2, markersize=0.3)
plt.axis('equal')
circle = Circle(xy=(ox,oy), radius=r, alpha=0.5)
ax.add_patch(circle)
plt.grid(ls='--')
print('pi={}'.format(pi))
plt.show()