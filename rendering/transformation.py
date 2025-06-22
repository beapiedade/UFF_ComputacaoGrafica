import math

class Transformation:
    @staticmethod
    def scaling(vertex, scale):
        x = vertex[0] * scale
        y = vertex[1] * scale
        z = vertex[2] * scale
        return (x, y, z)

    @staticmethod
    def x_rotation(vertex, angle):
        angle = math.radians(angle)
        x = vertex[0] 
        y = vertex[1] * math.cos(angle) - vertex[2] * math.sin(angle)
        z = vertex[1] * math.sin(angle) + vertex[2] * math.cos(angle)
        return (x, y, z)

    @staticmethod
    def y_rotation(vertex, angle):
        angle = math.radians(angle)
        x = vertex[0] * math.cos(angle) + vertex[2] * math.sin(angle)
        y = vertex[1]
        z = -vertex[0] * math.sin(angle) + vertex[2] * math.cos(angle)
        return (x, y, z)

    @staticmethod
    def z_rotation(vertex, angle):
        angle = math.radians(angle)
        x = vertex[0] * math.cos(angle) - vertex[1] * math.sin(angle)
        y = vertex[0] * math.sin(angle) + vertex[1] * math.cos(angle)
        z = vertex[2]
        return (x, y, z)

    @staticmethod
    def reflection(vertex, x_reflection, y_reflection, z_reflection):
        x = vertex[0] * x_reflection
        y = vertex[1] * y_reflection
        z = vertex[2] * z_reflection
        return (x, y, z)

    @staticmethod
    def shearing(vertex, x_shear, y_shear, z_shear):
        x = vertex[0] + vertex[1] * x_shear + vertex[2] * z_shear
        y = vertex[1] + vertex[0] * y_shear + vertex[2] * z_shear
        z = vertex[2] + vertex[0] * z_shear + vertex[1] * y_shear
        return (x, y, z)

    @staticmethod
    def translate(vertex, x_delta, y_delta, z_delta):
        x = vertex[0] + x_delta
        y = vertex[1] + y_delta
        z = vertex[2] + z_delta
        return (x, y, z)
    
    @staticmethod
    def to_cabinet(vertex, angle, factor):
        angle = math.radians(angle)
        x = vertex[0] - vertex[2] * factor * math.cos(angle)
        y = vertex[1] - vertex[2] * factor * math.sin(-angle/2)
        z = vertex[2]
        return (x, y, z)