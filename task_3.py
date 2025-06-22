import pygame
from rendering.converter import Converter
from rendering.primitives import Primitives
from rendering.projection import Projection
from rendering.colors import Colors

# Task 3: Render 3D objects with ilumination and shading
# set up the screen
width = 800
height = 800
origin = (width*0.10, height*0.80, 0)

# create the axes
x_axis, y_axis, z_axis = Projection.create_axis(origin, width, height, 63.4)

# create the objects
objects_origin = [[300, 100], [200, 50]]
objects_data = [
    ["primitives/beatriz/vertex.csv", "primitives/beatriz/face_vertices.csv"], 
    ["primitives/julia/vertex.csv", "primitives/julia/face_vertices.csv"]
]
objects = []
for i in range(len(objects_data)):
    # extract vertices
    object = objects_data[i]
    vertices = Converter.read_csv(object[0])
    vertices_list = Primitives.extract_vertices(vertices)

    # apply the 3D transformation
    new_origin = [origin[0] + objects_origin[i][0], origin[1] - objects_origin[i][1]]
    ajusted_vertices = Projection.to_pygame_3d_screen(vertices_list[1], new_origin, -63.4)
    #ajusted_vertices = Projection.to_pygame_screen(vertices_list[1], new_origin[0], new_origin[1])

    # extract faces
    faces = Converter.read_csv(object[1])
    faces_list = Primitives.extract_faces([vertices_list[0], ajusted_vertices], faces, 3)
    faces_list = Primitives.painters_algorithm(faces_list)
    objects.append(faces_list)

# create the colors
'''
objects_hsv_colors = [
    (280, 100, 100), 
    (30, 100, 100)
]
'''
objects_hsv_colors = [
    Colors.shading(len(objects[0][0]),280),
    Colors.shading(len(objects[1][0]),30)
]
objects_rgb_colors = [
    Colors.to_rgb(objects_hsv_colors[0]),
    Colors.to_rgb(objects_hsv_colors[1])
]

# initialize pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# run the main loop
running = True
while running:
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE)) or event.type == pygame.QUIT:
            running = False
        
    # paint the background
    screen.fill((255, 255, 255))

    # draw the axes
    pygame.draw.line(screen, (255, 0, 0), x_axis[0], x_axis[1], 1)
    pygame.draw.line(screen, (0, 255, 0), y_axis[0], y_axis[1], 1)
    pygame.draw.line(screen, (0, 0, 255), z_axis[0], z_axis[1], 1)

    # draw the objects
    for i in range(len(objects)):
        for j in range(len(objects[i][1])):
            pygame.draw.polygon(screen, objects_rgb_colors[i][j], objects[i][1][j], 0)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()