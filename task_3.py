import csv
import pygame
from rendering.primitives import Primitives
from rendering.projection import Projection
from rendering.transformation import Transformation
from rendering.colors import Colors

def read_csv(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        data = []
        for row in reader:
            data.append(row)
        return data

# Task 3: Alternate Colors Projection
width = 800
height = 800
origin_x = 600
origin_y = 200

objects_data = [["primitives/beatriz/vertex.csv", "primitives/beatriz/face_vertices.csv"], ["primitives/julia/vertex.csv", "primitives/julia/face_vertices.csv"]]
objects_faces = []
for obj in objects_data[1:]:
    vertices_list = Primitives.extract_vertices(read_csv(obj[0]))
    ajusted_vertices = Projection.to_pygame_screen(vertices_list[1], origin_x, origin_y)
    faces_list = Primitives.extract_2d_faces([vertices_list[0], ajusted_vertices], read_csv(obj[1]))
    objects_faces.append(faces_list)

objects_hsv_colors = [(180, 100, 100)]
objects_colors = Colors.to_rgb(objects_hsv_colors)

light_position = [0, 0, 1]
old_light_position = pygame.time.get_ticks()
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

    new_light_position = pygame.time.get_ticks()
    if (new_light_position - old_light_position > gap):
        light_position[0] += 0.1
        light_position[1] += 0.1
        light_position[2] += 0.1

    # draw object 1 faces
    for i in range(len(faces_list[1]), 0, -1):
        face = faces_list[1][i-1]
        pygame.draw.polygon(screen, objects_colors[0], face, 0)

    # draw light source
    pygame.draw.circle(screen, (255, 255, 0), (int(origin_x + light_position[0]), int(origin_y + light_position[1])), 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()