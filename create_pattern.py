import pygame
import math
import json


WIDTH, HEIGHT = 960, 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 30
run = True

pattern = [[None for x in range(43)] for y in range(39)]

hex_a = 12
hsin60 = hex_a * math.sin(math.radians(60))
colors = [(56, 189, 248), (251, 194, 57)]
while run:
    window.fill((15, 23, 42))
    mouse_coords = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_coords = pygame.mouse.get_pos() + (event.button,)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            with open("pattern.json", "w") as file:
                json.dump(pattern, file)
    
    for y in range(39):
        hex_y = (1.5 * hex_a + 1) * y
        for x in range(43):
            if y%2 == 0: hex_x = 2*(hsin60 + 1)*x
            else: hex_x = 2*(hsin60 + 1)*x + hsin60
            
            if mouse_coords != None and ((hex_x-mouse_coords[0])**2 + (hex_y-mouse_coords[1])**2)**0.5 < hex_a:
                if mouse_coords[2] == 1: pattern[y][x] = 0
                elif mouse_coords[2] == 3: pattern[y][x] = 1
            
            if pattern[y][x] != None:
                pygame.draw.polygon(window, colors[pattern[y][x]], [(hex_x, hex_y-hex_a), (hex_x + hsin60, hex_y - hex_a/2),
                                                    (hex_x + hsin60, hex_y + hex_a/2), (hex_x, hex_y + hex_a),
                                                (hex_x - hsin60, hex_y + hex_a/2), (hex_x - hsin60, hex_y - hex_a/2)])

            pygame.draw.polygon(window, (31, 40, 59), [(hex_x, hex_y-hex_a), (hex_x + hsin60, hex_y - hex_a/2),
                                                    (hex_x + hsin60, hex_y + hex_a/2), (hex_x, hex_y + hex_a),
                                                (hex_x - hsin60, hex_y + hex_a/2), (hex_x - hsin60, hex_y - hex_a/2)], 1)


    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
