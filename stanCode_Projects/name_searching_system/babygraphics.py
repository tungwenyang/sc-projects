"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

This program is to plot the historical trend of a
list of name from a given dict of baby name data
onto the canvas.
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
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


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
    return GRAPH_MARGIN_SIZE + year_index * (width - 2 * GRAPH_MARGIN_SIZE) / len(YEARS)


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, 0, GRAPH_MARGIN_SIZE, CANVAS_HEIGHT)

    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), 0, get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT)
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           text=YEARS[i], anchor=tkinter.NW)


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
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # Write your code below this line
    #################################
    for i in range(len(lookup_names)):
        d = name_data[lookup_names[i]]

        last_x = 0
        last_y = 0

        for j in range(len(YEARS)):
            # x coordinate
            current_x = get_x_coordinate(CANVAS_WIDTH, j)

            # y coordinate
            if str(YEARS[j]) in d:
                current_y = get_y_coordinate(CANVAS_HEIGHT, d[str(YEARS[j])])
            else:
                current_y = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE

            # create line if not YEAR[0]
            if j > 0:
                canvas.create_line(last_x, last_y, current_x, current_y, width=LINE_WIDTH, fill=COLORS[i % len(COLORS)])

            # create text
            if current_y == CANVAS_HEIGHT - GRAPH_MARGIN_SIZE:
                canvas.create_text(current_x + TEXT_DX, current_y, text=(lookup_names[i], '*'),
                                   anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])
            else:
                canvas.create_text(current_x + TEXT_DX, current_y, text=(lookup_names[i], d[str(YEARS[j])]),
                                   anchor=tkinter.SW, fill=COLORS[i % len(COLORS)])

            # assign current_x,_y as last_x,_y for next loop
            last_x, last_y = current_x, current_y


def get_y_coordinate(height, rank):
    """
    Given the height of the canvas and the rank of the current year
    to the associated name, returns the y coordinate.

    Input:
        height (int): The height of the canvas
        rank (str): The rank of the current year in the name_data[name] dict
    Returns:
        y_coordinate (int): The y coordinate associated with the rank of specified year.
    """
    if int(rank) <= MAX_RANK:
        return GRAPH_MARGIN_SIZE + int(rank) * (height - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK
    else:
        return height - GRAPH_MARGIN_SIZE


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
