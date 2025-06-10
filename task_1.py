import csv
import pygame
from rendering.colors import Colors
from rendering.primitives import Primitives
from rendering.transformation import Transformation

def read_csv(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        data = []
        for row in reader:
            data.append(row)
        return data

vertices_list = Primitives.extract_vertices(read_csv("primitives/vertex.csv"))
edges_list = Primitives.extract_edges(vertices_list, read_csv("primitives/edge.csv"))
faces_list = Primitives.extract_faces(vertices_list, read_csv("primitives/face_vertices.csv"))

# Task 1: Projeção do Esqueleto em Arame
width = 800
height = 800
origin_x = width // 2
origin_y = height // 2

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Projeção do Esqueleto em Arame)
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE)) or event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))

    # desenha as faces na tela
    for i in range(len(faces_list)):
        face = faces_list[i]
        pygame.draw.polygon(screen, color, face, 0)

    # escreve o texto na tela
    font = pygame.font.Font(None, 36)
    timestamp = font.render(f"Tempo: {old_colors / 1000:.1f} s", True, (255, 255, 255))
    timestamp_rect = timestamp.get_rect(topleft=(50, 50))
    screen.blit(timestamp, timestamp_rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()