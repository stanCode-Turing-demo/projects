"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing the inverse image of
mt-rainier.jpg below the original one
Name: 周尚樺 (Sean Chou)
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: filename is a string
    :return: return an image that has showed the mirror lake picture
    """
    img = SimpleImage(filename)
    new_image = SimpleImage.blank(img.width, img.height*2)
    for x in range(img.width):
        for y in range(img.height):
            pi = img.get_pixel(x, y)
            new_pixel1 = new_image.get_pixel(x, y)  # 將原圖的Pixel 丟到新製作的圖面對應到的位置
            new_pixel2 = new_image.get_pixel(x, img.width-1-y)  # 將原圖的Pixel 丟到新製作的圖面鏡像的位置
            new_pixel1.green = pi.green
            new_pixel1.blue = pi.blue
            new_pixel1.red = pi.red
            new_pixel2.green = pi.green
            new_pixel2.blue = pi.blue
            new_pixel2.red = pi.red
    return new_image


def main():
    """
    TODO: 顯示原本的照片後, 製作出一張鏡像的照片後顯示此照片
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
