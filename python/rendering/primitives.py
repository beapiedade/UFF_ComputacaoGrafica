from pygame import Vector3


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

    @staticmethod
    def painters_algorithm(faces, camera_position):
        distances = []
        for i in range(len(faces[0])):
            face = faces[1][i]
            x_centroid, y_centroid, z_centroid = 0, 0, 0
            for j in range(len(face)):
                vertex = face[j]
                x_centroid += vertex[0]
                y_centroid += vertex[1]
                z_centroid += vertex[2]
            n_vertices = len(face)
            centroid = (x_centroid / n_vertices, 
                        y_centroid / n_vertices, 
                        z_centroid / n_vertices)
            distance = ((centroid[0] - camera_position[0]) ** 2 + 
                        (centroid[1] - camera_position[1]) ** 2 + 
                        (centroid[2] - camera_position[2]) ** 2) ** 0.5
            distances.append((faces[0][i], faces[1][i],distance))
       
        distances.sort(key=lambda x: x[2], reverse=True)
        sorted_names = []
        sorted_faces = []
        for i in range(len(distances)):
            sorted_names.append(distances[i][0])
            sorted_faces.append(distances[i][1])
        return [sorted_names,sorted_faces]
    
    @staticmethod
    def to_pairs(faces):
        new_faces = []
        for face in faces[1]:
            new_vertices = []
            for vertex in face:
                new_vertices.append((vertex[0], vertex[1]))
            new_faces.append(new_vertices)
        return [faces[0], new_faces]
