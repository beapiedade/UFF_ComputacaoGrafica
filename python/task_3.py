import pygame, math
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
angle = 63.4
x_axis, y_axis, z_axis = Projection.create_axis(origin, width, height, angle)
camera = (100, 300, -200)

# create the objects
objects_origin = [[300, 200], [200, 150]]
objects_data = [
    ["python/primitives/beatriz/vertex.csv", "python/primitives/beatriz/face_vertices.csv"], 
    ["python/primitives/julia/vertex.csv", "python/primitives/julia/face_vertices.csv"]
]
objects = []
for i in range(len(objects_data)):
    # extract vertices
    object = objects_data[i]
    vertices = Converter.read_csv(object[0])
    vertices_list = Primitives.extract_vertices(vertices)

    # apply the 3D transformation
    new_origin = [origin[0] + objects_origin[i][0], origin[1] - objects_origin[i][1]]
    ajusted_vertices = Projection.to_pygame_3d_screen(vertices_list[1], new_origin, -angle)

    # extract faces
    faces = Converter.read_csv(object[1])
    faces_list = Primitives.extract_faces([vertices_list[0], ajusted_vertices], faces, 3)
    faces_list = Primitives.painters_algorithm(faces_list, camera)

    objects.append(faces_list)

#aqui vc determina onde a luz vai aparecer
x = camera[0]
y = camera[1]

# initialize pygame
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#iluminação
def criar_luz_gradiente(raio, cor):
    r = raio * 5
    brilho = pygame.Surface((r*2 , r*2 ), pygame.SRCALPHA) #aqui se vc deixar só (r,r) a luz fica triangular, no momento ela é um circulo posicionado na borda da tela

    for x in range(r * 2):
        for y in range(r * 2):
            dx, dy = x - r, y - r
            dist = math.sqrt(dx * dx + dy * dy)  
            if dist < r:
                alpha = int(255 * ((1 - dist / r) ** 3))  #aqui ajusta a suavidade
                brilho.set_at((x, y), (*cor, alpha))  
    return brilho

raio_luz = 200
luz = criar_luz_gradiente(raio_luz, (255, 241, 224))
light_position = camera

# create the colors
objects_hsv_colors = [
    Colors.shading(280, objects[0][1], light_position),
    Colors.shading(180, objects[1][1], light_position)
]
objects_rgb_colors = [
    Colors.to_rgb(objects_hsv_colors[0]),
    Colors.to_rgb(objects_hsv_colors[1])
]

# convert the objects to pairs
objects[0] = Primitives.to_pairs(objects[0])
objects[1] = Primitives.to_pairs(objects[1])

# run the main loop
running = True
while running:
    for event in pygame.event.get():
        if (event.type == pygame.KEYDOWN and (event.key == pygame.K_SPACE or event.key == pygame.K_ESCAPE)) or event.type == pygame.QUIT:
            running = False
        
    # paint the background
    screen.fill((0, 0, 0))

    # draw the axes
    pygame.draw.line(screen, (255, 0, 0), x_axis[0], x_axis[1], 1)
    pygame.draw.line(screen, (0, 255, 0), y_axis[0], y_axis[1], 1)
    pygame.draw.line(screen, (0, 0, 255), z_axis[0], z_axis[1], 1)

    # draw the objects
    for i in range(len(objects)):
        for j in range(len(objects[i][1])):
            pygame.draw.polygon(screen, objects_rgb_colors[i][j], objects[i][1][j], 0)

    #screen.blit(luz, (x, y))

    pygame.draw.circle(screen, (255, 255, 0), (x,y), 5)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()