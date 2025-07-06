import pygame
from rendering.converter import Converter
from rendering.primitives import Primitives
from rendering.projection import Projection
from rendering.colors import Colors

# Task 2: Alternate Colors Projection
width = 800
height = 800
origin_x = width // 2
origin_y = height // 2

vertices_list = Primitives.extract_vertices(Converter.read_csv("python/primitives/julia/vertex.csv"))
ajusted_vertices = Projection.to_pygame_screen(vertices_list[1], origin_x, origin_y)
faces_list = Primitives.extract_faces([vertices_list[0], ajusted_vertices], Converter.read_csv("python/primitives/julia/face_vertices.csv"), 2)

hsv_colors = Colors.generate_hsv(len(faces_list[0]))
colors_sequence = Colors.to_rgb(hsv_colors)
old_colors = pygame.time.get_ticks()
gap = 500 

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Alternate Colors Projection")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE)) or event.type == pygame.QUIT:
            running = False
        
    screen.fill((0, 0, 0))
    pygame.draw.line(screen, (255, 0, 0), (0, origin_y), (width, origin_y), 1)
    pygame.draw.line(screen, (0, 255, 0), (origin_x, 0), (origin_x, height), 1)

    # rotate colors of faces
    new_colors = pygame.time.get_ticks()
    if (new_colors - old_colors > gap):
        first_color = colors_sequence.pop(0)
        colors_sequence.append(first_color)
        old_colors = new_colors

    # draw faces
    for i in range(len(faces_list[1]), 0, -1):
        face = faces_list[1][i-1]
        color = colors_sequence[i-1]
        pygame.draw.polygon(screen, color, face, 0)

    # write timestamp on the screen
    font = pygame.font.Font(None, 36)
    timestamp = font.render(f"Tempo: {old_colors / 1000:.1f} s", True, (255, 255, 255))
    timestamp_rect = timestamp.get_rect(topleft=(50, 50))
    screen.blit(timestamp, timestamp_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()