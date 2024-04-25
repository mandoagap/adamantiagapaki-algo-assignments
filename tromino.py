import argparse
# Define command-line arguments for matrix of 
parser = argparse.ArgumentParser(description="Recursive Backtracking Tromino Tiling")
parser.add_argument("-n", "--size", type=int, default=2, help="Size of the matrix (default: 3)")

args = parser.parse_args()
print(args.size)

X = 0
Y = 0
N = 2 ** args.size
grid = [['X' for i in range(N)] for j in range(N)]
# grid[Y][X] = -1
symbols = list(range(N*N))

# Time complexity: O(N^2 * log(N))
# Space complexity: O(N^2)

def tilling(n, x, y, a, b, i, colors):
    '''
    n : size of grid
    a,b,c,d : corners of quartile
    x, y : position of filled tile in current quartile
    i : i'th tile
    colors : dictionary to keep track of colors used in each quartile
    '''
    show()

    # Base Case -> place 3 OTHER Tiles
    if n == 2:
        if n not in colors:
            colors[n] = ['R', 'G', 'B']
        if x-a < n//2 and y-b >= n//2:
            grid[b+n//2-1][a+n//2-1] = colors[n][i % 3]
            grid[b+n//2-1][a+n//2] = colors[n][i % 3]
            grid[b+n//2][a+n//2] = colors[n][i % 3]
        if x-a >= n//2 and y-b >= n//2:
            grid[b+n//2-1][a+n//2-1] = colors[n][i % 3]
            grid[b+n//2-1][a+n//2] = colors[n][i % 3]
            grid[b+n//2][a+n//2-1] = colors[n][i % 3]
        return

    # Place Middle Tromino
    if n not in colors:
        colors[n] = ['R', 'G', 'B']
    current_color = colors[n][i % 3]

    
    #if x-a >= n//2 and y-b < n//2:
        grid[b+n//2-1][a+n//2-1] = current_color
        grid[b+n//2][a+n//2] = current_color
        grid[b+n//2][a+n//2-1] = current_color
    if x-a < n//2 and y-b >= n//2:
        grid[b+n//2-1][a+n//2-1] = current_color
        grid[b+n//2-1][a+n//2] = current_color
        grid[b+n//2][a+n//2] = current_color

    i += 1
    # Recursion
    if x-a < n//2 and y-b < n//2:
        tilling(n//2, x, y, a, b, i, colors)
        tilling(n//2, a+n//2, b+n//2-1, a+n//2, b, i, colors)
        tilling(n//2, a+n//2, b+n//2, a+n//2, b+n//2, i, colors)
        tilling(n//2, a+n//2-1, b+n//2, a, b+n//2, i, colors)
    if x-a >= n//2 and y-b < n//2:
        tilling(n//2, a+n//2-1, b+n//2-1, a, b, i, colors)
        tilling(n//2, x, y, a+n//2, b, i, colors)
        tilling(n//2, a+n//2, b+n//2, a+n//2, b+n//2, i, colors)
        tilling(n//2, a+n//2-1, b+n//2, a, b+n//2, i, colors)


# Visualize the output of matrix filled with R or G or B
def show():
    for i in grid:
        for j in i:
            if j == -1:
                print(' X', end=' ')
            else:
                print(' ' + str(j), end=' ')
        print()
    print()


tilling(N, X, Y, 0, 0, 0, {})
print("Final : ")
show()

with open("tromino_tiling_grid_{}x{}.txt".format(N, N), 'w') as f:
    f.write('\n'.join([' '.join(map(str, row)) for row in grid]))