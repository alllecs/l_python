#!/usr/bin/python3

import math
import matplotlib.pyplot as plt

from matplotlib.patches import Circle, Wedge, Polygon, Ellipse, Arc, Path, PathPatch

plt.xlim(0, 13)
plt.ylim(0, 13)
ax = plt.gca()
figure = Circle((6, 7),5)

#figure = arc((6, 6), 5, 3, 0, 200, 100)

ax.add_patch(figure)
plt.show()


