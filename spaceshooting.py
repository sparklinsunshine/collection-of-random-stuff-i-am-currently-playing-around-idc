import pygame
import random

# Initialize pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the player
player_img = pygame.image.load("D:\kinnudata\python_files\spaceship.png")
player_width, player_height = player_img.get_rect().size
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 20
player_speed = 6 

# Set up enemies
enemy_img = pygame.image.load("D:\kinnudata\python_files\\alien.png")
enemy_width, enemy_height = enemy_img.get_rect().size
enemy_speed = 3
enemies = []
spawn_delay = 120

# Set up bullets
bullet_img = pygame.image.load("D:\kinnudata\python_files\\bullet.png")
bullet_width, bullet_height = bullet_img.get_rect().size
bullet_speed = 7
bullets = []

# Set up the clock
clock = pygame.time.Clock()

# Set up the score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Shoot bullets
    if keys[pygame.K_SPACE]:
        if len(bullets) < 3:
            bullets.append([player_x + player_width // 2 - bullet_width // 2, player_y])

    # Spawn enemies
    if spawn_delay == 0:
        enemy_x = random.randint(0, WIDTH - enemy_width)
        enemy_y = -enemy_height
        enemies.append([enemy_x, enemy_y])
        spawn_delay = 150

    # Move enemies
    for enemy in enemies:
        enemy[1] += enemy_speed
        if enemy[1] > HEIGHT:
            enemies.remove(enemy)

    # Handle collisions
    for bullet in bullets:
        bullet[1] -= bullet_speed
        for enemy in enemies:
            if pygame.Rect(enemy[0], enemy[1], enemy_width, enemy_height).colliderect(
                    pygame.Rect(bullet[0], bullet[1], bullet_width, bullet_height)):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 1
            else:
                continue

    # Draw everything
    screen.fill(BLACK)
    screen.blit(player_img, (player_x, player_y))
    for enemy in enemies:
        screen.blit(enemy_img, (enemy[0], enemy[1]))
    for bullet in bullets:
        screen.blit(bullet_img, (bullet[0], bullet[1]))

    # Display the score
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Decrement spawn delay
    if spawn_delay > 0:
        spawn_delay -= 1

    # Cap the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
