#! /usr/bin/env python

from Ghadah import Random
import numpy as np
import matplotlib.pyplot as plt

random_number = Random(77777777)
myx =[]
for i in range(0,15000):
    myx.append(random_number.Rayleigh())


plt.figure()
plt.hist(myx, 50, density=True, facecolor='r', alpha=0.75)

plt.xlabel('t')
plt.ylabel('Probability')
plt.title('Uniform random number')
plt.grid(True)


plt.savefig("Uniform_random_number.png")
plt.show()
