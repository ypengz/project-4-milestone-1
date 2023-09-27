import random
import pygame
import math
import sys

"""ENTER YOUR UF-ID BELOW"""
rng_seed = 12345678

random.seed(rng_seed)

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
BG = (123, 123, 123)
COLORS = []
for i in range(14):
    R = random.randint(0, 1) * 255
    G = random.randint(0, 1) * 255
    B = random.randint(0, 1) * 255
    newColor = (R, G, B)
    COLORS.append(newColor)

# Line math
lineTheta = random.randint(0, 11) * (math.pi/6)
LINE_END = (WIDTH//2 + int(175*math.cos(lineTheta)), HEIGHT//2 + int(175*math.sin(lineTheta)))

# Create a display screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Test Demo")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG)  # Fill the screen with white
    theta = 0
    for i in range(12):
        pos = (WIDTH//2 + int(200*math.cos(theta)), HEIGHT//2 + int(200*math.sin(theta)))
        theta += math.pi/6
        pygame.draw.circle(screen, COLORS[i], pos, 30)  # Draw the edge dots
    pygame.draw.line(screen, COLORS[12], (WIDTH // 2, HEIGHT // 2), LINE_END, 30) # Draw the hand
    pygame.draw.circle(screen, COLORS[13], (WIDTH//2, HEIGHT//2), 50)  # Draw a blue circle (dot) in the center
    pygame.display.flip()  # Update the display

    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
