"""
SC101 - Assignment3
Adapted from Nick Parlante's Ghost assignment by
Jerry Liao.

-----------------------------------------------

This program can compare several photos,
find out the best pixel,
and export a new photo with no sundries or strangers.
(photos which need to be compared should be the same size)
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the square of the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): squared distance between red, green, and blue pixel values

    """
    red_dist = (red - pixel.red) ** 2
    green_dist = (green - pixel.green) ** 2
    blue_dist = (blue - pixel.blue) ** 2
    dist = (red_dist + green_dist + blue_dist) ** 0.5
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]
    """
    red_total = 0
    green_total = 0
    blue_total = 0
    for pixel in pixels:
        red_total += pixel.red
        green_total += pixel.green
        blue_total += pixel.blue
    # Use the total amount of the color value // the amount of pixels to get average.
    rgb = [red_total // len(pixels), green_total//len(pixels), blue_total//len(pixels)]
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages
    """
    rgb = get_average(pixels)
    smallest_dist = get_pixel_dist(pixels[0], rgb[0], rgb[1], rgb[2])
    best = pixels[0]
    for pixel in pixels:
        dist = get_pixel_dist(pixel, rgb[0], rgb[1], rgb[2])
        # Compare each pixel's distance, and record the smallest one.
        if dist < smallest_dist:
            best = pixel
    return best


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    # Using for loop to record every pixel in several images.
    # Each time pick pixels in the same (x, y) in different images.
    for x in range(width):
        for y in range(height):
            pixels = []
            for image in images:
                pixels += [image.get_pixel(x, y)]
            best = get_best_pixel(pixels)
            new_pixel = result.get_pixel(x, y)
            new_pixel.red = best.red
            new_pixel.green = best.green
            new_pixel.blue = best.blue
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    """
    This program use the 'load_images()' function to load photos,
    and then use the 'solve()' function to create a new image without sundries or strangers.
    """
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
