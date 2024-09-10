import random

import pygame

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch the Apples")
pygame.time.wait(5000)

# Colors
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Player (Green Square)
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - player_size
player_speed = 5

# Falling Apple (Red Square)
apple_size = 30
apple_x = random.randint(0, screen_width - apple_size)
apple_y = 0
apple_speed = 5

# Score
score = 0
miss = 0
font = pygame.font.SysFont("", 36)
lost = font.render("YOU LOST", True, (0, 0, 0))
win = font.render("YOU WON", True, (0, 0, 0))

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Check for events (keyboard, quit, etc.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
        player_x += player_speed

    # Move the apple
    apple_y += apple_speed

    # If the apple goes off screen, reset it
    if apple_y > screen_height:
        apple_x = random.randint(0, screen_width - apple_size)
        apple_y = 0

    # Check for collision (player catches apple)
    if player_x <= apple_x + apple_size and player_x + player_size >= apple_x and player_y < apple_y + apple_size:
        score += 1
        apple_x = random.randint(0, screen_width - apple_size)
        apple_y = 0

    # Check for miss (player misses apple)
    if apple_y == screen_height:
        miss += 1

    # Fill the screen with white
    screen.fill(white)

    # Draw the player (green square)
    pygame.draw.rect(screen, green,
                     (player_x, player_y, player_size, player_size))

    # Draw the apple (red square)
    pygame.draw.rect(screen, red, (apple_x, apple_y, apple_size, apple_size))

    # Draw the score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Draw the miss
    miss_text = font.render(f"Miss: {miss}", True, (0, 0, 0))
    screen.blit(miss_text, (10, 40))

    # Update the display
    pygame.display.update()

    # Set the frame rate
    clock.tick(30)

    if miss >= 5:
        screen.blit(lost, (screen_width // 2 - 50, screen_height // 2))
        pygame.display.update()
        pygame.time.wait(5000)
        break

    if score >= 10:
        screen.blit(win, (screen_width // 2 - 50, screen_height // 2))
        pygame.display.update()
        pygame.time.wait(5000)
        break

# Quit Pygame
pygame.quit()
