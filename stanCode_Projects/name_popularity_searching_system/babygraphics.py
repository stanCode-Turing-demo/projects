"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

This program can show a line chart(with name, rank and years on it)
when users type the names.
The rank of the name data is based on the dictionary 'name_data' in babynames.py.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]  # A list of several filename.
CANVAS_WIDTH = 1000  # The width of the canvas.
CANVAS_HEIGHT = 600  # The height of the canvas.
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]  # A list of the years.
GRAPH_MARGIN_SIZE = 20  # Distance between the line and the canvas margin.
COLORS = ['red', 'purple', 'green', 'blue']  # A list of colors which used to change line color and text color.
TEXT_DX = 2  # Distance between line and text.
LINE_WIDTH = 2  # The width of the line.
MAX_RANK = 1000  # The upper bound of the rank.


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x_coordinate = ((width - GRAPH_MARGIN_SIZE*2)/len(YEARS) * year_index) + GRAPH_MARGIN_SIZE
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # Add the upper horizontal line on canvas.
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    # Add the lower horizontal line on canvas.
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)
    # Add vertical lines and the text(years).
    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(x+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i],
                           anchor=tkinter.NW, font='times 15')


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    # 'proportion' is the range between 2 horizontal lines / MAX_RANK(constant)
    proportion = (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE*2) / MAX_RANK
    for i in range(len(lookup_names)):
        if lookup_names[i] in name_data:
            data = name_data[lookup_names[i]]  # 'data' is a dictionary. (data = {year:rank, ......})
            pre_rank = -1  # 'pre_rank' record the rank in the previous year. (But the first rank is a )
            for j in range(len(YEARS)):
                # If the name is in the data, record the rank into 'ranking'.
                # 'rank' is an int, the y position on canvas
                # 'rank_text' is a str, which will be added on canvas
                if str(YEARS[j]) in data:
                    ranking = data[str(YEARS[j])]
                    rank = int(ranking)*proportion + GRAPH_MARGIN_SIZE
                    rank_text = str(lookup_names[i] + ' ' + ranking)
                else:
                    rank = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                    rank_text = str(lookup_names[i] + ' *')
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, j)+TEXT_DX, rank,
                                   text=rank_text, anchor=tkinter.SW, font='times 15', fill=COLORS[i % len(COLORS)])
                # The line cannot be defined if there's only one point.
                if pre_rank != -1 and j != 0:
                    canvas.create_line(get_x_coordinate(CANVAS_WIDTH, j-1), pre_rank,
                                       get_x_coordinate(CANVAS_WIDTH, j), rank, width=LINE_WIDTH,
                                       fill=COLORS[i % len(COLORS)])
                pre_rank = rank  # Record the rank in the previous year.


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
