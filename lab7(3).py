import pygame
import sys


pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Ball Movement with Image")


ball_image = pygame.image.load("ball.png").convert_alpha()
ball_image = pygame.transform.scale(ball_image, (50, 50))  
ball_rect = ball_image.get_rect()
ball_rect.center = (WIDTH // 2, HEIGHT // 2)

STEP = 20

running = True
while running:
    screen.fill((255, 255, 255))  

    
    screen.blit(ball_image, ball_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if ball_rect.left - STEP >= 0:
            ball_rect.x -= STEP
    if keys[pygame.K_RIGHT]:
        if ball_rect.right + STEP <= WIDTH:
            ball_rect.x += STEP
    if keys[pygame.K_UP]:
        if ball_rect.top - STEP >= 0:
            ball_rect.y -= STEP
    if keys[pygame.K_DOWN]:
        if ball_rect.bottom + STEP <= HEIGHT:
            ball_rect.y += STEP

    pygame.display.flip()
    clock.tick(20)

pygame.quit()
sys.exit()
