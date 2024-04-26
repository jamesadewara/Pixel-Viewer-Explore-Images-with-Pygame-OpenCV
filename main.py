import pygame
from pygame.locals import *
import cv2
import numpy as np

# Initialize pygame
pygame.init()

# Define some colors and screen dimensions
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = (800, 640)

# Determines the size of the text
TEXT_SIZE = 1

# Create a pygame screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SCREEN DEMO COMPLEX")

# Flag to control the main loop
isRunning = True

# Load an image using OpenCV
image = cv2.imread("james.png")

# Flip the image horizontally
image = cv2.flip(image, flipCode=1)

# Convert the image to grayscale
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Get the dimensions of the image
imageHeight, imageWidth, channel = image.shape

# Create a blank surface with the same dimensions as the image
blank = np.zeros(image.shape, dtype=np.uint8)
originalImg = pygame.surfarray.make_surface(blank)

# Create a container surface to hold the image
container = pygame.surface.Surface((originalImg.get_width(), originalImg.get_height()))

# Set the initial position of the container
containerRect = container.get_rect(center=(WIDTH / 2, HEIGHT / 2))

# Fill the container with black color
container.fill(BLACK)

# Create a font object
font = pygame.font.SysFont(None, size=TEXT_SIZE)

# Initialize y position
y = -1

# Main loop
while isRunning:
    # Event handling loop
    for event in pygame.event.get():
        # Check if the user wants to quit
        if event.type == pygame.QUIT:
            isRunning = False
            pygame.quit()

    # Fill the screen with white color
    screen.fill(WHITE)
    
    # Blit the container onto the screen
    screen.blit(container, containerRect)

    try:
        # Check if we've reached the end of the image
        if y >= imageHeight:
            pass
        else:
            # Move down one row
            y += 1
            # Loop through each pixel in the row
            for x in range(imageWidth):
                # Loop through each color channel
                for j in range(channel):
                    # Render the pixel value as text and blit it onto the container
                    container.blit(font.render(str(image[y][x][j]), True, (image[y][x])), (x, y))
    except:
        pass

    # Update the display
    pygame.display.update()
