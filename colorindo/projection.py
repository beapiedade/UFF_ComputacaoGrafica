class Projection:
    @staticmethod
    def change_scale(vertex, scale):
        x = vertex[0] * scale
        y = vertex[1] * scale
        return (x, y)
    
    @staticmethod
    def change_origin(vertex, origin_x, origin_y):
        x = vertex[0] + origin_x
        y = vertex[1] + origin_y
        return (x, y)
    
    @staticmethod
    def change_orientation(vertex, x_orientation, y_orientation): 
        x = vertex[0] * x_orientation
        y = vertex[1] * y_orientation
        return (x, y)