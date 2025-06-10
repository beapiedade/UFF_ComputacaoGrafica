from rendering import Colors, Transformation
from screen import Screen

# arestas
a1 = (a, b)
a2 = (a, c)
a3 = (a, d)
a4 = (a, e)
a5 = (a, f)
a6 = (a, g)
a7 = (b, h)
a8 = (c, i)
a9 = (d, j)
a10 = (e, k)
a11 = (f, l)
a12 = (g, m)
a13 = (b, c)
a14 = (c, d)
a15 = (d, e)
a16 = (e, f)
a17 = (f, g)
a18 = (g, b)
a19 = (h, i)
a20 = (i, j)
a21 = (j, k)
a22 = (k, l)
a23 = (l, m)
a24 = (m, h)

# faces formadas por pontos
f1 = (a, b, c)
f2 = (a, c, d)
f3 = (a, d, e)
f4 = (a, e, f)
f5 = (a, f, g)
f6 = (a, g, b)
f7 = (b, h, i, c)
f8 = (c, i, j, d)
f9 = (d, j, k, e)
f10 = (e, k, l, f)
f11 = (f, l, m, g)
f12 = (g, m, h, b)
f13 = (h, m, l, k, j, i)
faces = [f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13]

# gera as cores cores hsv
hsv_colors = Colors.generate_hsv(len(faces))

# converte as cores para o rgb
rgb_colors = Colors.convert_to_rgb(hsv_colors)

# ajusta o sistema de coordenadas, aumenta a escala e translada pra origem
transformed_faces = []
for face in faces:
    transformed_face = []
    for vertex in face:
        oriented_vertex = Projection.change_orientation(vertex, 1, -1)
        scaled_vertex = Projection.change_scale(oriented_vertex, 40)
        translated_vertex = Projection.change_origin(scaled_vertex, Screen.origin_x, Screen.origin_y)
        transformed_face.append(translated_vertex)
    transformed_faces.append(transformed_face)

# exibe a projeção paralela
Screen.display(Screen, transformed_faces, rgb_colors, 10000)