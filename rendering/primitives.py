class Primitives:
    @staticmethod
    def extract_vertices(data):
        names = []
        coordinates = []
        for vertex in data:
            names.append(vertex[0])
            coordinates.append(tuple(map(float, vertex[1:])))
        return [names, coordinates]

    @staticmethod
    def extract_edges(vertices, data):
        names = []
        coordinates = []
        for edge in data:
            names.append(edge[0])
            edge_coordinates = []
            for vertex in edge[1:]:
                v_index = vertices[0].index(vertex)
                edge_coordinates.append(vertices[1][v_index])
            coordinates.append(edge_coordinates)
        return [names, coordinates]

    @staticmethod
    def extract_faces(vertices, data, points):
        names = []
        coordinates = []
        for face in data:
            names.append(face[0])
            face_coordinates = []
            for vertex in face[1:]:
                v_index = vertices[0].index(vertex)
                face_coordinates.append(vertices[1][v_index][:points])
            coordinates.append(face_coordinates)
        return [names, coordinates]

    def painters_algorithm(faces):
        sorted_z = []
        for i in range(len(faces[0])):
            face = faces[1][i]
            z_sum = 0
            for j in range(len(face)):
                vertex = face[j]
                z_sum += vertex[2]
                faces[1][i][j] = (vertex[0], vertex[1])
            sorted_z.append((faces[0][i], z_sum / len(faces[1][i])))
        sorted_z.sort(key=lambda x: x[1], reverse=True)
        sorted_names = []
        sorted_faces = []
        for i in range(len(sorted_z)):
            index = faces[0].index(sorted_z[i][0])
            sorted_names.append(faces[0][index])
            sorted_faces.append(faces[1][index])
        #sorted_names.reverse()
        #sorted_faces.reverse()
        return [sorted_names,sorted_faces]
