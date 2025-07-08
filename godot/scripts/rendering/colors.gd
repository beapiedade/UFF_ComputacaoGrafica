class_name Colors
extends RefCounted

static func generate_hsv(n: int) -> Array:
	var hsv_colors = []
	for i in range(n):
		var hue = i / float(n)
		var saturation = 1.0
		var value = 1.0
		var color = Vector3(hue, saturation, value)
		hsv_colors.append(color)
	return hsv_colors

static func to_rgb(colors: Array) -> Array:
	var rgb_colors = []
	for color in colors:
		rgb_colors.append(Color.from_hsv(color[0], color[1], color[2]))
	return rgb_colors

static func calculate_shading(vertices: Array, light_position: Vector3, hue: float, max_light_distance: float) -> Color:
	if vertices.is_empty() or max_light_distance <= 0:
		return Color.BLACK

	# calcula o centroide da face
	var centroid = Vector3.ZERO
	for v in vertices:
		centroid += v
	centroid /= vertices.size()

	# calcula a distância do centroide até a luz
	var distance = centroid.distance_to(light_position)

	# calcula o brilho de forma linear e absoluta.
	var brightness = 1.0 - (distance / max_light_distance)
	brightness = clamp(brightness, 0.0, 1.0)
	
	# cria a cor final a partir do HSV
	var final_color = Color.from_hsv(hue, 1.0, brightness)

	return final_color
