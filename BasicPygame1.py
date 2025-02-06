import pygame
import random
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Juego de Plataforma: Desafíos de Código')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 24)

player_width = 50
player_height = 60
player_x = 100
player_y = 500
player_vel = 5
player_jump = 10
player_is_jumping = False
player_jump_count = 10

ground_height = 50
platforms = [(0, SCREEN_HEIGHT - ground_height, SCREEN_WIDTH, ground_height)]

def desafio_programacion():
    print("¡Desafío de código!")
    print("Resuelve el siguiente reto para continuar:")
    print("¿Cuál es el resultado de 5 + 3?")
    respuesta = input("Escribe tu respuesta: ")
    if respuesta == "8":
        return True
    else:
        return False

player = pygame.Rect(player_x, player_y, player_width, player_height)

def draw_player(player):
    pygame.draw.rect(screen, GREEN, player)

def move_player(keys, player):
    if keys[pygame.K_LEFT]:
        player.x -= player_vel
    if keys[pygame.K_RIGHT]:
        player.x += player_vel
    if not player_is_jumping:
        if keys[pygame.K_SPACE]:
            jump(player)

def jump(player):
    global player_is_jumping, player_jump_count
    player_is_jumping = True
    player.y -= player_jump_count * 2

def apply_gravity(player):
    global player_is_jumping, player_jump_count
    if player_is_jumping:
        if player_jump_count >= -10:
            neg = 1
            if player_jump_count < 0:
                neg = -1
            player.y -= (player_jump_count ** 2) * 0.4 * neg
            player_jump_count -= 1
        else:
            player_is_jumping = False
            player_jump_count = 10

def draw_platforms():
    for platform in platforms:
        pygame.draw.rect(screen, BLACK, pygame.Rect(platform))

def game_loop():
    global player_x, player_y
    run = True
    while run:
        screen.fill(WHITE)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys = pygame.key.get_pressed()
        
        move_player(keys, player)
        
        apply_gravity(player)

        draw_platforms()

        for platform in platforms:
            if player.colliderect(pygame.Rect(platform)):
                player.y = platform[1] - player.height
                player_is_jumping = False
                player_jump_count = 10

        draw_player(player)

        if player.x > 500 and player.x < 600: 
            if desafio_programacion():  
                platforms.append((600, SCREEN_HEIGHT - ground_height, SCREEN_WIDTH, ground_height))  

        pygame.display.update()
        clock.tick(60)

game_loop()

pygame.quit()
