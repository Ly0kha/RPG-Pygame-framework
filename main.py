# Import necessary libraries
import pygame

# Initialize pygame
pygame.init()

# Set screen size and caption
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Runebebe")

# Load player image
player_image = pygame.image.load("player.png")
player_x = 400
player_y = 500

# Load enemy image
enemy_image = pygame.image.load("enemy.png")
enemy_x = 200
enemy_y = 200

# Load item image
item_image = pygame.image.load("item.png")
item_x = 600
item_y = 400

# Set level
level = 1

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
   
    # Move player
    player_x += 1
    player_y += 1

    # Move enemy
    enemy_x -= 1
    enemy_y -= 1

    # Check for collision with item
    if player_x > item_x and player_x < item_x + 50 and player_y > item_y and player_y < item_y + 50:
        print("Player collected item!")

    # Draw player, enemy, and item on screen
    screen.blit(player_image, (player_x, player_y))
    screen.blit(enemy_image, (enemy_x, enemy_y))
    screen.blit(item_image, (item_x, item_y))

    # Update level bar
    level_bar = pygame.draw.rect(screen, (255, 0, 0), (750, 10, 30, level))

    # Update display
    pygame.display.update()

# Quit pygame
pygame.quit()
