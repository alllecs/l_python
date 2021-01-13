#!/usr/bin/python3

import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge, Polygon, Ellipse, Arc, Path, PathPatch

n = 8
m = 7

plt.xlim(0, n)
plt.ylim(0, m)
ax = plt.gca()

vertices = [(1, 3), (7, 2), (6, 1), (3, 1), (1, 3), (4, 2.5), (4,6), (7, 3), (4,2.5)]
codes = [1, 2, 2, 2, 2, 1, 2, 2, 2]

path = Path(vertices, codes)
path_patch = PathPatch(path, lw = 3)

ax.add_patch(path_patch)
plt.show()


