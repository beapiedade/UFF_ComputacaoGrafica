import csv
from rendering.primitives import Primitives
from rendering.transformation import Transformation

def read_csv(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        data = []
        for row in reader:
            data.append(row)
        return data


vertices_list = Primitives.extract_vertices(read_csv("primitives/julia/vertex.csv"))
ajusted_vertices = []
for a in vertices_list[1]:
    ajusted_vertices.append(Transformation.x_rotation(a, -90))

for b in range(len(vertices_list[0])):
    print(f'{vertices_list[0][b]},{ajusted_vertices[b][0]},{ajusted_vertices[b][1]},{ajusted_vertices[b][2]}')