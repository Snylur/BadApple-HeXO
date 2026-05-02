import pygame
import math
import json


WIDTH, HEIGHT = 960, 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 30


hex_a = 12
hsin60 = hex_a * math.sin(math.radians(60))
colors = [(56, 189, 248), (251, 194, 57)]
pattern = json.load(open("pattern.json", "r"))
for i in range(1, 6573):
    window.fill((15, 23, 42))

    stri = "0"*(4-len(str(i))) + str(i)
    frame = pygame.image.load(f"frames/output_{stri}.jpg")
    
    for y in range(39):
        hex_y = (1.5 * hex_a + 1) * y
        for x in range(43):
            if y%2 == 0: hex_x = 2*(hsin60 + 1)*x
            else: hex_x = 2*(hsin60 + 1)*x + hsin60

            if not frame.get_at((min(479, int(hex_x/2)), min(359, int(hex_y/2))))[0] < 128:
                pygame.draw.polygon(window, colors[pattern[y][x]], [(hex_x, hex_y-hex_a), (hex_x + hsin60, hex_y - hex_a/2),
                                            (hex_x + hsin60, hex_y + hex_a/2), (hex_x, hex_y + hex_a),
                                            (hex_x - hsin60, hex_y + hex_a/2), (hex_x - hsin60, hex_y - hex_a/2)])
            pygame.draw.polygon(window, (31, 40, 59), [(hex_x, hex_y-hex_a), (hex_x + hsin60, hex_y - hex_a/2),
                                                    (hex_x + hsin60, hex_y + hex_a/2), (hex_x, hex_y + hex_a),
                                                (hex_x - hsin60, hex_y + hex_a/2), (hex_x - hsin60, hex_y - hex_a/2)], 1)


    pygame.display.update()
    pygame.image.save(window, f"hexo-frames/output_{stri}.jpg")
    clock.tick(FPS)

pygame.quit()
