from tromino_tilling import tilling  # Corrected function name import
from PIL import Image, ImageDraw
import re

def create_image(grid, filename):  # Added grid as argument
    color_map = {'R': (255, 0, 0), 'G': (0, 255, 0), 'B': (0, 0, 255), 'X': (255, 255, 255)}
    cell_size = 50  # Adjust the size of each cell as needed
    image_size = (len(grid[0]) * cell_size, len(grid) * cell_size)
    image = Image.new("RGB", image_size, color=(255, 255, 255))
    draw = ImageDraw.Draw(image)

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            color = color_map[cell]
            draw.rectangle([x * cell_size, y * cell_size, (x + 1) * cell_size, (y + 1) * cell_size], fill=color)

    image.save(filename)
    image.show()