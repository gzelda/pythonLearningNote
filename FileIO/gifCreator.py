import imageio
def create_gif(image_list, gif_name, duration = 1.0):
    '''
    :param image_list: 这个列表用于存放生成动图的图片
    :param gif_name: 字符串，所生成gif文件名，带.gif后缀
    :param duration: 图像间隔时间
    :return:
    '''
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))

    imageio.mimsave(gif_name, frames, 'GIF', duration=duration)
    return

def main():
    #这里放上自己所需要合成的图片


    image_list = []
    for i in range(10):
        filename = "Velocity/"+str(i)+'.jpg'
        image_list.append(filename)

    print(image_list)

    #image_list = ['1.jpg', '2.jpg', '3.jpg']
    gif_name = "Velocity/"+"V1.gif"
    duration = 1
    create_gif(image_list, gif_name, duration)

if __name__ == '__main__':
    main()