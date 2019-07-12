import matplotlib.pyplot as plt
import numpy as np

"""

"""
class polarRing:
    def __init__(self, thetaNum = 20, tickNum = 5, tickMax = 2):
        self.thetan = thetaNum
        self.tickn = tickNum
        self.tickm = tickMax
        self.figure = plt.figure()

    def getFig(self):
        return self.figure


    def drawHeatMap(self, data, alpha1, alpha2):

        self.figure.clear()
        theta, r = np.mgrid[0:2 * np.pi:21j, 0:2:6j]  # 6 = tickn+1    21 = thetaNum+1
        z = np.random.random(theta.size).reshape(theta.shape)
        ## print(theta.size,theta.shape)
        #fig, ax = plt.subplots(1, 1, subplot_kw=dict(projection='polar'))
        axes = plt.subplot(111, polar=True)
        # cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
        cmap = plt.cm.get_cmap("YlOrRd")
        # cmap.set_under("yellow")
        # cmap.set_over("red")
        ims = []
        c = axes.pcolormesh(theta, r, data, cmap=cmap)



        self.figure.colorbar(c, ax=axes)
        axes.set_title('Velocity')

        axes.set_ylim([0, self.tickm])
        axes.set_yticklabels([])

        l1, = axes.plot([0, alpha1], [0, 2], color='blue', linestyle='dashed')
        l2, = axes.plot([0, alpha2], [0, 2], color='blue', linestyle='dashed')

        bars = axes.bar((alpha1+alpha2)/2+np.pi, 2, width=np.pi*2 - abs(alpha1-alpha2), bottom=0.0)

        #ims.append((c,))
        #ims.append((l1,))
        #ims.append((l2,))
        #ims.append((bars,))

        for bar in bars:
            bar.set_facecolor('black')
            bar.set_alpha(0.5)
        #print("axes:",axes)
        return self.figure, axes, ims



if __name__ == '__main__':

    pr = polarRing()
    for i in range(1,10):
        data = np.random.random(126).reshape((21, 6))
        pr.drawHeatMap(data, np.pi / 6, np.pi / 3)
        plt.savefig(str(i)+".jpg")

    plt.show()