import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set dimensions of the grid
width, height = 900, 900
cell_size = 10

# Create the display surface
screen = pygame.display.set_mode((width, height))

# Calculate the number of cells in each direction
cols = width // cell_size
rows = height // cell_size

# Create an empty grid
grid = np.random.choice([0, 1], size=(cols, rows))

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)

# Main game loop
running = True
while running:
    new_grid = grid.copy()

    screen.fill(black)

    for x in range(cols):
        for y in range(rows):
            if grid[x, y] == 1:
                pygame.draw.rect(screen, white, (x * cell_size, y * cell_size, cell_size, cell_size))
            else:
                pygame.draw.rect(screen, black, (x * cell_size, y * cell_size, cell_size, cell_size))

    for x in range(cols):
        for y in range(rows):
            # Count live neighbors
            neighbors = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                         (x, y - 1), (x, y + 1),
                         (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]

            live_neighbors = sum(grid[i % cols, j % rows] for i, j in neighbors)

            # Apply the rules of the Game of Life
            if grid[x, y] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[x, y] = 0
            else:
                if live_neighbors == 3:
                    new_grid[x, y] = 1

    grid = new_grid.copy()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
