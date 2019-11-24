#tutorial: https://matplotlib.org/3.1.1/tutorials/introductory/pyplot.html
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4]) # plot assumes these are sequence of y values, hence zero index
plt.ylabel('some numbers')
plt.show()

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro') # default style is black line 'b-', can use red dots
plt.axis([0, 6, 0, 20])
plt.show()

import numpy as np # python by itself useless for numeric processing. matplotlib converts/uses numpy arrays internally
# evenly sampled time at 200ms intervals
np.arange(10)np.arange(10)
t = np.arange(0., 5., 0.2)
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()

#can use keywords strings if data object allows access of variables with strings
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data) # c=color s = marker size
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()


#sankey diagram (household budget)
from matplotlib.sankey import Sankey
fig = plt.figure(figsize = (15,8))
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[], 
                     title="Household Budget")
sankey = Sankey(ax=ax, scale=.1, offset=1, unit='%')
sankey.add(flows=[100, -50, -30, -20],
           labels=['household budget', 'necessities', 'fun', 
                   'saving'],
           orientations=[0, 0, 1, -1],
           trunklength = 10,
           edgecolor = '#027368',
           facecolor = '#027368')
sankey.add(flows=[50, -30, -10, -10], 
           labels=['','rent', 'groceries', 'other'],
           trunklength = 2,
           pathlengths = [3,3,3,3],
           orientations=[0, 1, 0, -1], 
           prior=0, #which sankey are you connecting to (0-indexed)
           connect=(1, 0), #flow number to connect: (prior, this)
           edgecolor = '#58A4B0',
           facecolor = '#58A4B0')
diagrams = sankey.finish()
plt.show()
