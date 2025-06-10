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