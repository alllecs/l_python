#!/usr/bin/python3

import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge, Polygon, Ellipse, Arc, Path, PathPatch

n = 6
m = 5

plt.xlim(0, n)
plt.ylim(0, m)
ax = plt.gca()

figure_w = Wedge((3, 1), 2, 45, 135)
ax.add_patch(figure_w)

figure_a = Arc((3, 1), 6, 6, 0, 45, 135, lw=3)
ax.add_patch(figure_a)

plt.show()


