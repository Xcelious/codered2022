import matplotlib.cm as cm
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import matplotlib.patches as mpatches

from matplotlib.collections import PatchCollection

patches = []

fig, ax = plt.subplots()

plt.title("Rover's Offline Map")
ax.set_xlim(-100, 100)
ax.set_ylim(-100, 100)

xline = lines.Line2D([0, 0], [-100, 100],
                    lw=1, color='black', axes=ax)

yline = lines.Line2D([-100, 100], [0, 0],
                    lw=1, color='black', axes=ax)

hotelzone = mpatches.Circle((0, 0), 15, facecolor='none', linewidth=5)
hotelzone.set_facecolor("black")
patches.append(hotelzone)

echzone = mpatches.Circle((-50, 7), 9)
patches.append(echzone)

im = plt.imshow(np.random.random((100, 100)),
                origin='lower', cmap=cm.winter,
                interpolation='spline36',
                extent=([-1, 1, -1, 1]))
im.set_clip_path(hotelzone)


collection = PatchCollection(patches, cmap=plt.cm.hsv, alpha=0.3)
ax.add_collection(collection)


ax.add_line(xline)
ax.add_line(yline)


plt.grid()
plt.tight_layout()

plt.show()