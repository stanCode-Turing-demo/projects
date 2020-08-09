"""
File: fire.py
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation
Name: 周尚樺 (Sean Chou)
"""
from simpleimage import SimpleImage

HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: filename is a string
    :return: return an image that has showed the highlighted picture
    """
    img = SimpleImage(filename)
    for pixel in img:
        avg = (pixel.red + pixel.blue + pixel.green)/3
        if pixel.red > avg*HURDLE_FACTOR:
            pixel.red = 255
            pixel.blue = 0
            pixel.green = 0
        else:
            pixel.red = avg
            pixel.blue = avg
            pixel.green = avg

    return img


def main():
    """
    TODO:
    This file contains a method called highlight_fires which detects the
    pixels that are recognized as fire and highlights them for better observation
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
