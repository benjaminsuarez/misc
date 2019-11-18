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
