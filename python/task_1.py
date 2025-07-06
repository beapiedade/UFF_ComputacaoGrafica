import pygame
from rendering.converter import Converter
from rendering.primitives import Primitives
from rendering.projection import Projection
from rendering.transformation import Transformation

# Task 1: Wireframe Projection
width = 800
height = 800
origin_x = width // 2
origin_y = height // 2

vertical_rotation = 0
horizontal_rotation = 0
rotate = False

@staticmethod
def update_orientation(vertices_list, vertical_angle, horizontal_angle):
    named_vertices = vertices_list[0]
    rotated_vertices = []
    for vertex in vertices_list[1]:
        vertex = Transformation.x_rotation(vertex, vertical_angle)
        vertex = Transformation.y_rotation(vertex, horizontal_angle)
        rotated_vertices.append(vertex)

    projected_vertices = Projection.to_pygame_screen(rotated_vertices, origin_x, origin_y)
    return Primitives.extract_edges([named_vertices, projected_vertices], Converter.read_csv("python/primitives/julia/edge.csv"))

vertices_list = Primitives.extract_vertices(Converter.read_csv("python/primitives/julia/vertex.csv"))
ajusted_vertices = Projection.to_pygame_screen(vertices_list[1], origin_x, origin_y)
edges_list = Primitives.extract_edges([vertices_list[0],ajusted_vertices], Converter.read_csv("python/primitives/julia/edge.csv"))

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Wireframe Projection")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE)) or event.type == pygame.QUIT:
            running = False
        
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP):
            vertical_rotation += 45
            rotate = True
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
            horizontal_rotation += 45
            rotate = True
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN):
            vertical_rotation -= 45
            rotate = True
        elif (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
            horizontal_rotation -= 45
            rotate = True

    if rotate:
        edges_list = update_orientation(vertices_list, vertical_rotation, horizontal_rotation)
        rotate = False

    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (255, 0, 0), (0, origin_y), (width, origin_y), 1)
    pygame.draw.line(screen, (0, 255, 0), (origin_x, 0), (origin_x, height), 1)

    # draw edges
    for i in range(len(edges_list[1]), 0, -1):
        edge = edges_list[1][i-1]
        pygame.draw.line(screen, (0, 0, 0), edge[0][:2], edge[1][:2], 1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()