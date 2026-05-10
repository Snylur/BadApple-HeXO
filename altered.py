import pygame
import math
import json
import random
random.seed(42)
choose = random.choice
shuff = random.shuffle
color = lambda: random.randint(0, 1)

WIDTH, HEIGHT = 960, 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 30
valids = []
can = lambda x: all([1<=_[0]-(_[1]-1)//2<42 and 1<=_[1]<38 for _ in x])
for y in range(1, 42):
    for p in range(1, 38):
        x = p + (y-1)//2
        j = 0
        valids.append([(x+j, y+i) for i in range(6)])
        valids.append([(x+i, y+j) for i in range(6)])
        valids.append([(x+i, y+i) for i in range(6)])
valids = list(filter(can, valids))
hex_a = 12
hsin60 = hex_a * math.sin(math.radians(60))
colors = [(56, 189, 248), (251, 194, 57)]












for i in range(1, 6573): # 6573
    print(i)
    window.fill((15, 23, 42))

    stri = "0" * (4 - len(str(i))) + str(i)
    frame = pygame.image.load(f"frames/output_{stri}.jpg")
    l = set()





    for y in range(1, 38):  # 39
        hex_y = (1.5 * hex_a + 1) * y
        for x in range(1, 42):
            if y % 2 == 0:
                hex_x = 2 * (hsin60 + 1) * x
            else:
                hex_x = 2 * (hsin60 + 1) * x + hsin60

            if not frame.get_at((min(479, int(hex_x / 2)), min(359, int(hex_y / 2))))[0] < 128:
                l.add((x + (y-1)//2, y))

    similar = lambda a, b: sum(_ in a for _ in b)
    contains = lambda a, b: similar(a, b) == len(b)
    if not any(contains(l, valid) for valid in valids):
        shuff(valids)
        valid = max(valids, key=lambda x: similar(x, l))
        l.update(valid)
    l = list(l)
    # print(l)
    available = list(filter(lambda x: contains(l, x), valids))
    hexing = lambda a, v: a[v[0]]==a[v[1]]==a[v[2]]==a[v[3]]==a[v[4]]==a[v[5]];
    while True:
        assignment = {_: color() for _ in l}
        while True:
            flag = False
            for valid in available:
                if hexing(assignment, valid):
                    flag = True
                    assignment[choose(valid)] ^= 1
            if not flag: break
        k = choose(available)
        c = color()
        for _ in k:
            assignment[_] = c
        total = 0
        for valid in available:
            if hexing(assignment, valid):
                total += 1
        if total == 1: break





    for y in range(1, 38):  # 39
        hex_y = (1.5 * hex_a + 1) * y
        for x in range(1, 42):
            if y % 2 == 0:
                hex_x = 2 * (hsin60 + 1) * x
            else:
                hex_x = 2 * (hsin60 + 1) * x + hsin60

            # we should by now be having a list of x y values to assign to
            # dirs can be either +x, +y, or, +x +y

            if (x + (y-1)//2, y) in assignment:
                pygame.draw.polygon(window, colors[assignment[(x + (y-1)//2, y)]], [(hex_x, hex_y-hex_a), (hex_x + hsin60, hex_y - hex_a/2),
                                            (hex_x + hsin60, hex_y + hex_a/2), (hex_x, hex_y + hex_a),
                                            (hex_x - hsin60, hex_y + hex_a/2), (hex_x - hsin60, hex_y - hex_a/2)])
            pygame.draw.polygon(window, (31, 40, 59) if (x + (y-1)//2, y) not in k else (255, 0, 0), [(hex_x, hex_y-hex_a), (hex_x + hsin60, hex_y - hex_a/2),
                                                    (hex_x + hsin60, hex_y + hex_a/2), (hex_x, hex_y + hex_a),
                                                (hex_x - hsin60, hex_y + hex_a/2), (hex_x - hsin60, hex_y - hex_a/2)], 1 if (x + (y-1)//2, y) not in k else 4)


    pygame.display.update()
    pygame.image.save(window, f"altered-frames/output_{stri}.jpg")
    clock.tick(FPS)

pygame.quit()
