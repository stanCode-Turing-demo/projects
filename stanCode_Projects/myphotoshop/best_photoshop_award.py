"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the 2020 Best
Photoshop Award for SC101P.
Please put all the images you use in image_contest folder
and make sure to choose which award you are aiming at
Name: 周尚樺(Sean Chou)
"""

from simpleimage import SimpleImage
GREEN_SCREEN = 1.46
X_EQUAL_PART = 10
X_PART = 3


def main():
    """
    TODO:

    """
    bg = SimpleImage("image_contest/background_1.jpg")
    fg = SimpleImage("image_contest/myself.jpg")
    bg.make_as_big_as(fg)
    result = combine(bg, fg)
    result.show()


def combine(back, me):
    """
    : param1 back: SimpleImage, the background image
    : param2 ma: SimpleImage, green screen figure image
    : return me: SimpleImage, the green screen pixels are replaced by pixels background image
    """
    for y in range(back.height):
        for x in range(back.width):
            pixel_me = me.get_pixel(x, y)
            if x < back.width//5:  # 裁切x 軸的前1/5全都做成背景
                pixel_bg = back.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
            elif y < back.height//10:  # 裁切y 軸的上半部全都做成背景
                pixel_bg = back.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
            elif y > back.height//10*9:  # 裁切y 軸的下半部1/10 的部分, 全都做成背景
                pixel_bg = back.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
            elif y < back.height//10*1.5 and x > back.width//3*2:  # 裁切右上角的一小部分, 做成背景
                pixel_bg = back.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
            elif pixel_me.green > pixel_me.blue*GREEN_SCREEN:  # 設定green 大於blue 的GREEN_SCREEN倍的像素換成背景像素
                pixel_bg = back.get_pixel(x, y)
                pixel_me.red = pixel_bg.red
                pixel_me.blue = pixel_bg.blue
                pixel_me.green = pixel_bg.green
    return me


if __name__ == '__main__':
    main()
