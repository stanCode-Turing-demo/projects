"""
File: blur.py
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
Name: 周尚樺(Sean Chou)
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, the image you would like to make it blurred
    :return: SimpleImage, the image has been blurred
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width-1):
        for y in range(img.height-1):
            if x == 0 and y == 0:  # 當像素在左上角的時候平均周遭的三個像素
                pixel = img.get_pixel(x, y)
                pixel_8 = img.get_pixel(x+1, y+1)
                pixel_5 = img.get_pixel(x + 1, y)
                pixel_7 = img.get_pixel(x, y+1)
                new_pixel = new_img.get_pixel(x, y)
                new_pixel.green = (pixel.green+pixel_5.green + pixel_7.green + pixel_8.green) / 4
                new_pixel.blue = (pixel.blue+pixel_5.blue + pixel_7.blue + pixel_8.blue) / 4
                new_pixel.red = (pixel.red+pixel_5.red + pixel_7.red + pixel_8.red) / 4
            elif x == 0 and y < img.height:  # 當像素在左邊的線時,只平均周遭的的五個像素
                pixel = img.get_pixel(x, y)
                pixel_2 = img.get_pixel(x, y - 1)
                pixel_3 = img.get_pixel(x+1, y-1)
                pixel_5 = img.get_pixel(x + 1, y)
                pixel_7 = img.get_pixel(x, y + 1)
                pixel_8 = img.get_pixel(x + 1, y + 1)
                new_pixel = new_img.get_pixel(x, y)
                new_pixel.green = (pixel.green + pixel_2.green + pixel_3.green + pixel_5.green + pixel_7.green +
                                   pixel_8.green)/6
                new_pixel.blue = (pixel.blue + pixel_2.blue + pixel_3.blue + pixel_5.blue + pixel_7.blue +
                                  pixel_8.blue)/6
                new_pixel.red = (pixel.red + pixel_2.red + pixel_3.red + pixel_5.red + pixel_7.red + pixel_8.red)/6
            elif y == 0:  # 當像素上方的線時,只平均周遭的的五個像素
                pixel = img.get_pixel(x, y)
                pixel_4 = img.get_pixel(x - 1, y)
                pixel_5 = img.get_pixel(x + 1, y)
                pixel_6 = img.get_pixel(x - 1, y + 1)
                pixel_7 = img.get_pixel(x, y + 1)
                pixel_8 = img.get_pixel(x + 1, y + 1)
                new_pixel = new_img.get_pixel(x, y)
                new_pixel.green = (pixel.green + pixel_4.green +
                                   pixel_5.green + pixel_6.green + pixel_7.green + pixel_8.green)/6
                new_pixel.blue = (pixel.blue + pixel_4.blue +
                                  pixel_5.blue + pixel_6.blue + pixel_7.blue + pixel_8.blue)/6
                new_pixel.red = (pixel.red + pixel_4.red +
                                 pixel_5.red + pixel_6.red + pixel_7.red + pixel_8.red)/6
            elif x == img.width and y == img.height:  # 當像素在最右下角時只平均周圍的三個像素
                pixel = img.get_pixel(x, y)
                pixel_1 = img.get_pixel(x - 1, y - 1)
                pixel_2 = img.get_pixel(x, y - 1)
                pixel_4 = img.get_pixel(x - 1, y)
                new_pixel = new_img.get_pixel(x, y)
                new_pixel.green = (pixel.green + pixel_1.green + pixel_2.green + pixel_4.green) / 4
                new_pixel.blue = (pixel.blue + pixel_1.blue + pixel_2.blue + pixel_4.blue) / 4
                new_pixel.red = (pixel.red + pixel_1.red + pixel_2.red + pixel_4.red) / 4
            elif x == img.width and y < img.height: # 當像素在右邊的線時,只平均周遭的的五個像素
                pixel = img.get_pixel(x, y)
                pixel_1 = img.get_pixel(x - 1, y - 1)
                pixel_2 = img.get_pixel(x, y - 1)
                pixel_4 = img.get_pixel(x - 1, y)
                pixel_6 = img.get_pixel(x - 1, y + 1)
                pixel_7 = img.get_pixel(x, y + 1)
                new_pixel = new_img.get_pixel(x, y)
                new_pixel.green = (pixel.green + pixel_1.green + pixel_2.green + pixel_4.green +
                                   pixel_6.green + pixel_7.green) / 6
                new_pixel.blue = (pixel.blue + pixel_1.blue + pixel_2.blue + pixel_4.blue +
                                  pixel_6.blue + pixel_7.blue) / 6
                new_pixel.red = (pixel.red + pixel_1.red + pixel_2.red + pixel_4.red +
                                 pixel_6.red + pixel_7.red) / 6
            elif y == img.height:  # 當像素沿著底線走的時候只平均周圍的六個像素
                pixel = img.get_pixel(x, y)
                pixel_1 = img.get_pixel(x - 1, y - 1)
                pixel_2 = img.get_pixel(x, y - 1)
                pixel_3 = img.get_pixel(x + 1, y - 1)
                pixel_4 = img.get_pixel(x - 1, y)
                pixel_5 = img.get_pixel(x + 1, y)
                new_pixel = new_img.get_pixel(x, y)
                new_pixel.green = (pixel.green + pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green +
                                   pixel_5.green) / 6
                new_pixel.blue = (pixel.blue + pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue +
                                  pixel_5.blue) / 6
                new_pixel.red = (pixel.red + pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red +
                                 pixel_5.red) / 6
            else:  # 當像素中間的時候,平均周圍的八個像素
                pixel = img.get_pixel(x, y)
                pixel_1 = img.get_pixel(x-1, y-1)
                pixel_2 = img.get_pixel(x, y-1)
                pixel_3 = img.get_pixel(x+1, y-1)
                pixel_4 = img.get_pixel(x-1, y)
                pixel_5 = img.get_pixel(x+1, y)
                pixel_6 = img.get_pixel(x-1, y+1)
                pixel_7 = img.get_pixel(x, y+1)
                pixel_8 = img.get_pixel(x+1, y+1)
                new_pixel = new_img.get_pixel(x, y)
                new_pixel.green = (pixel.green+pixel_1.green+pixel_2.green+pixel_3.green+pixel_4.green+
                                   pixel_5.green+pixel_6.green+pixel_7.green+pixel_8.green)/9
                new_pixel.blue = (pixel.blue+pixel_1.blue+pixel_2.blue+pixel_3.blue+pixel_4.blue+
                                  pixel_5.blue+pixel_6.blue+pixel_7.blue+pixel_8.blue)/9
                new_pixel.red = (pixel.red+pixel_1.red+pixel_2.red+pixel_3.red+pixel_4.red+
                                 pixel_5.red+pixel_6.red+pixel_7.red+pixel_8.red)/9
    return new_img


def main():
    """
    TODO: 將一張照片模糊化, 先顯示模糊前的照片, 在顯示模糊化後的照片
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
