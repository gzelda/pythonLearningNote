import matplotlib.pyplot as plt
import numpy as np

"""

"""
class polarRing:
    def __init__(self, thetaNum = 20, tickNum = 5, tickMax = 2):
        self.thetan = thetaNum
        self.tickn = tickNum
        self.tickm = tickMax
    def drawHeatMap(self, data, alpha1, alpha2):
        theta, r = np.mgrid[0:2 * np.pi:21j, 0:2:6j]   #6 = tickn+1    21 = thetaNum+1
        z = np.random.random(theta.size).reshape(theta.shape)
        ## print(theta.size,theta.shape)
        fig, ax = plt.subplots(1, 1, subplot_kw=dict(projection='polar'))
        #cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
        cmap = plt.cm.get_cmap("YlOrRd")
        #cmap.set_under("yellow")
        #cmap.set_over("red")

        c = ax.pcolormesh(theta, r,  data, cmap=cmap)
        fig.colorbar(c, ax=ax)
        ax.set_title('Velocity')

        ax.set_ylim([0, self.tickm])
        ax.set_yticklabels([])

        plt.plot([0, alpha1], [0, 2], color='blue', linestyle='dashed')
        plt.plot([0, alpha2], [0, 2], color='blue', linestyle='dashed')

        bars = ax.bar((alpha1+alpha2)/2+np.pi, 2, width=np.pi*2 - abs(alpha1-alpha2), bottom=0.0)

        for bar in bars:
            bar.set_facecolor('black')
            bar.set_alpha(0.5)



if __name__ == '__main__':

    pr = polarRing()
    data = np.random.random(126).reshape((21,6))
    print(data)
    pr.drawHeatMap(data, np.pi/6, np.pi/3)

    plt.show()