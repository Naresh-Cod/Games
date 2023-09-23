import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 900
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
SNAKE_SPEED = 11

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Curve Fever")

# Snake class
class Snake:
    def __init__(self):
        self.body = [(5, 5)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0

    def move(self):
        new_head = (self.body[0][0] + self.direction[0], self.body[0][1] + self.direction[1])
        self.body.insert(0, new_head)

    def grow(self):
        self.score += 1

    def collide(self):
        return self.body[0] in self.body[1:]

    def update(self):
        self.move()
        if self.collide():
            pygame.quit()
            sys.exit()

# Food class
class Food:
    def __init__(self):
        self.position = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))

    def spawn(self):
        self.position = (random.randint(0, GRID_WIDTH-1), random.randint(0, GRID_HEIGHT-1))

# Create snake and food
snake = Snake()
food = Food()

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != DOWN:
                snake.direction = UP
            elif event.key == pygame.K_DOWN and snake.direction != UP:
                snake.direction = DOWN
            elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                snake.direction = LEFT
            elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                snake.direction = RIGHT

    snake.update()

    if snake.body[0] == food.position:
        snake.grow()
        food.spawn()

    screen.fill(WHITE)

    for segment in snake.body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    pygame.draw.rect(screen, GREEN, pygame.Rect(food.position[0] * GRID_SIZE, food.position[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    pygame.display.flip()
    clock.tick(SNAKE_SPEED)
