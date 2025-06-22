import colorsys

class Colors:
    @staticmethod
    def generate_hsv(N):
        hsv_list = []
        for i in range(1, N+1):
            hue = 360 * i / (N+1)
            hsv = (hue, 100, 100)
            hsv_list.append(hsv)
        return hsv_list
    
    @staticmethod
    def shading(hue, faces, light_position):
        distances = []
        for face in faces:
            x_centroid, y_centroid, z_centroid = 0, 0, 0
            for vertex in face:
                x_centroid += vertex[0]
                y_centroid += vertex[1]
                z_centroid += vertex[2]
            n_vertices = len(face)
            centroid = (x_centroid / n_vertices, 
                        y_centroid / n_vertices, 
                        z_centroid / n_vertices)
            distance = ((centroid[0] - light_position[0]) ** 2 + 
                        (centroid[1] - light_position[1]) ** 2 + 
                        (centroid[2] - light_position[2]) ** 2) ** 0.5
            distances.append(distance)

        hsv_list = []
        max_distance = max(distances)
        for distance in distances:
            value = 100 - distance / max_distance * 100
            hsv = (hue, 100, value)
            hsv_list.append(hsv)
        return hsv_list
    
    @staticmethod
    def to_rgb(hsv_list):
        rgb_list = []
        for hsv in hsv_list:
            h_normalized = hsv[0] / 360
            s_normalized = hsv[1] / 100
            v_normalized = hsv[2] / 100
            rgb_normalized = colorsys.hsv_to_rgb(h_normalized, s_normalized, v_normalized)

            r = int(rgb_normalized[0] * 255)
            g = int(rgb_normalized[1] * 255)
            b = int(rgb_normalized[2] * 255)
            rgb_list.append((r, g, b))
        return rgb_list