import pygame
import random

# Initialize Pygame
pygame.init()

# Set dimensions of the display
width, height = 800, 600

# Create the display surface
screen = pygame.display.set_mode((width, height))

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

# Define simulation parameters
ant_count = 20
food_count = 5
pheromone_decay = 0.95
pheromone_drop = 0.1


# Define classes for Ant and Food
class Ant:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = black
        self.has_food = False

    def move(self):
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 5)


class Food:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = green

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), 10)


# Create lists to store ants and food
ants = [Ant(random.randint(0, width), random.randint(0, height)) for _ in range(ant_count)]
foods = [Food(random.randint(0, width), random.randint(0, height)) for _ in range(food_count)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(white)

    # Update and draw ants
    for ant in ants:
        if ant.has_food:
            ant.color = green
        else:
            ant.color = black

        # Move ants towards food
        if not ant.has_food:
            nearest_food = min(foods, key=lambda f: ((ant.x - f.x) ** 2 + (ant.y - f.y) ** 2) ** 0.5)
            ant.x += int((nearest_food.x - ant.x) / 10)
            ant.y += int((nearest_food.y - ant.y) / 10)

        ant.move()
        ant.draw()

    # Update and draw food
    for food in foods:
        food.draw()

    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()
