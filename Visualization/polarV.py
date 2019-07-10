"""
Demo of a line plot on a polar axis.
"""
import numpy as np
from matplotlib import pyplot as plt

r = np.arange(0, 2, 0.01)
theta = 2 * np.pi * r

ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)

ax.set_rmax(2)
ax.set_rticks([0.4, 0.8, 1.2, 1.6, 2])  # less radial ticks
ax.set_rlabel_position(-22.5)  # get radial labels away from plotted line
ax.grid(True)

ax.set_title("velocity Dynamic", va='top')
plt.show()