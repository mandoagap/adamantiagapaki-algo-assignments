from draw_tromino_tiling import tilling  # Corrected function name import
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



def extract_grid_size_from_filename(filename):
    match = re.search(r'_([0-9]+)x([0-9]+)\.png$', filename)
    if match:
        width = int(match.group(1))
        height = int(match.group(2))
        return width, height
    else:
        return None

filename = "tromino_tiling_image_4x4.png"
grid_width, grid_height = extract_grid_size_from_filename(filename)
print("Grid size extracted from filename:", grid_width, "x", grid_height)

# Now let's call the create_image function with the correct grid size
grid = [['X', 'R', 'R', 'B'], ['R', 'G', 'G', 'B'], ['R', 'G', 'G', 'B'], ['R', 'R', 'B', 'X']]
create_image(grid, filename)