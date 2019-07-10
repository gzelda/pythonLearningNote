# normal API

[matlibplt api doc](https://matplotlib.org/3.1.1/api/index.html)
[pyplot api doc](https://matplotlib.org/3.1.1/api/pyplot_summary.html)

## 构图
plt.figure(num=,figsize=(len,width),)  添加后续画图句柄
plt.xlim((s,e))
plt.ylim((s,e))
plt.xlable ylabel

plt.xticks(np.linspace(-1,1,5))  坐标单位间隔
plt.yticks([0,1,2,3,4,],[r'$zero$',"one","two","three","four"])

#### subplot

plt.subplot(r,c,p)  rows colomns position 也可以写成rcp的形式

ax1 = plt.subplot2grid((3,3),((0,0)),colspan=3,rowspan=1)
subplot2grid(mapsize,originPoint,colspan,rowspan)

#### 极坐标
subplots(projection='polar')


#### gca
ax = plt.gca()   get current axis
ax.spines['right'].       脊梁
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',-1))

## 画图 

#### plot
plt.plot(x,y,color=,linestyle=,linewidth=)

#### pcolor

ax.pcolor([x,y], z ,cmap=) 前两个参数为坐标（可以为极坐标，取决于ax的类型）  z为数值，渲染出的颜色与cmap的选择有关
pcolormesh 渲染高维数值
colorbar 渲染颜色栏
[colormap渐变的网址代号](https://matplotlib.org/users/colormaps.html)


## 描述
#### legend

l1, = plt.plot(...., label=*"description words"*)
l2, = plt.plot(...., label=*"description words"*)
plt.legend(,handles=[l1,l2],labels=,loc='best')    图例    
