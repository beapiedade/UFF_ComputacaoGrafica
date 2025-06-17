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
    def extract_faces(vertices, data):
        names = []
        coordinates = []
        for face in data:
            names.append(face[0])
            face_coordinates = []
            for vertex in face[1:]:
                v_index = vertices[0].index(vertex)
                face_coordinates.append(vertices[1][v_index])
            coordinates.append(face_coordinates)
        return [names, coordinates]
    
    @staticmethod
    def extract_2d_faces(vertices, data):
        names = []
        coordinates = []
        for face in data:
            names.append(face[0])
            face_coordinates = []
            for vertex in face[1:]:
                v_index = vertices[0].index(vertex)
                v_coordinates = vertices[1][v_index]
                face_coordinates.append(v_coordinates[:2])
            coordinates.append(face_coordinates)
        return [names, coordinates]