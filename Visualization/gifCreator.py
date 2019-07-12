import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from Visualization.polarRing import polarRing

ims = []

N = 10
data = np.random.random(126*N).reshape((N, 21, 6))
pr = polarRing()

fig = pr.getFig()

for i in range(1, N-1):
    #print(data[i])
    fig1, axes, im = pr.drawHeatMap(data[i], 0, 1)
    #im = plt.scatter(1, 1).findobj()

    print(im)
    #print(im)
    ims.append(im)

print(np.shape(ims), ims)
ani = animation.ArtistAnimation(fig, ims, interval=50, repeat_delay=1000,blit=True)
plt.show()
#ani.save("test1.gif", writer='pillow')
