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
