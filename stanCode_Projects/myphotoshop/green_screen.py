"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in ReyGreenScreen.png
Name: 周尚樺(Sean Chou)
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, the background image
    :param figure_img: SimpleImage, the RayGreenScreen.png
    :return: SimpleImage, Put Ray's photo into the Millennium Falcon space ship
    """
    new_image = SimpleImage.blank(figure_img.width, figure_img.height)  # 取得一張白的畫布
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            pixel = figure_img.get_pixel(x, y)
            new_pixel = background_img.get_pixel(x, y)
            new_image_pixel = new_image.get_pixel(x, y)
            bigger = max(pixel.blue, pixel.red)  # 判斷Ray 照片中的像素Blue 跟Red 數值誰比較大
            if bigger*2 < pixel.green:
                new_image_pixel.blue = new_pixel.blue
                new_image_pixel.green = new_pixel.green
                new_image_pixel.red = new_pixel.red
            else:
                new_image_pixel.blue = pixel.blue
                new_image_pixel.green = pixel.green
                new_image_pixel.red = pixel.red
    return new_image


def main():
    """
    TODO: 讀取兩張圖片, 將兩張圖片合成成一張圖片
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
