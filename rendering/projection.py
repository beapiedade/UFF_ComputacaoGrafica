from rendering.transformation import Transformation

class Projection:
    @staticmethod
    def to_pygame_screen(vertices_list, origin_x, origin_y, origin_z=0):
        new_vertices = []
        for vertex in vertices_list:
            transformed_vertex = Transformation.reflection(vertex, 1, -1, 1)
            transformed_vertex = Transformation.scaling(transformed_vertex, 40)
            transformed_vertex = Transformation.translate(transformed_vertex, origin_x, origin_y, 0)
            new_vertices.append(transformed_vertex)
        return new_vertices
    
    @staticmethod 
    def change_orientation(vertices_list, angle, axis):
        new_vertices = []
        if (axis == "x"):
            for vertex in vertices_list:
                vertex = Transformation.x_rotation(vertex, angle)
                new_vertices.append(vertex)
        else: 
            for vertex in vertices_list:
                vertex = Transformation.y_rotation(vertex, angle)
                new_vertices.append(vertex)
        return new_vertices
    
    @staticmethod
    def update_projection(vertices_list, origin_x, origin_y):
        new_vertices = []
        for vertex in vertices_list:
            transformed_vertex = Transformation.reflection(vertex, 1, -1, 1)
            transformed_vertex = Transformation.translate(vertex, origin_x, origin_y, 0)
            new_vertices.append(transformed_vertex)
        return new_vertices
