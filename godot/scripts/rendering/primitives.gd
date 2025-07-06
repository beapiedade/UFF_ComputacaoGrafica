class_name Primitives
extends RefCounted

static func read_csv(file_path: String) -> Array:
	var file = FileAccess.open(file_path, FileAccess.READ)
	var data = []
	if file:
		while not file.eof_reached():
			var line = file.get_csv_line()
			if line.size() > 0:
				data.append(line)
	return data

static func extract_vertices(data: Array) -> Array:
	var names = []
	var coordinates = []
	for vertex_data in data:
		names.append(vertex_data[0])
		var coords_str = vertex_data.slice(1)
		var coords = []
		for c in coords_str:
			coords.append(float(c))
		coordinates.append(Vector3(coords[0], coords[1], coords[2]))
	return [names, coordinates]

static func extract_edges(vertices: Array, data: Array) -> Array:
	var names = []
	var coordinates = []
	var vertex_names = vertices[0]
	var vertex_coords = vertices[1]
	for edge_data in data:
		names.append(edge_data[0])
		var edge_coordinates = []
		for vertex_name in edge_data.slice(1):
			var v_index = vertex_names.find(vertex_name)
			if v_index != -1:
				edge_coordinates.append(vertex_coords[v_index])
		coordinates.append(edge_coordinates)
	return [names, coordinates]

static func extract_faces(vertices: Array, data: Array) -> Array:
	var names = []
	var coordinates = []
	var vertex_names = vertices[0]
	var vertex_coords = vertices[1]
	for face_data in data:
		names.append(face_data[0])
		var face_coordinates = []
		for vertex_name in face_data.slice(1):
			var v_index = vertex_names.find(vertex_name)
			if v_index != -1:
				var v = vertex_coords[v_index]
				face_coordinates.append(v)
		coordinates.append(face_coordinates)
	return [names, coordinates]

static func get_normalization_scale_factor(vertices_coords: Array) -> float:
	if vertices_coords.is_empty():
		return 1.0

	var aabb = AABB(vertices_coords[0], Vector3.ZERO)
	
	for i in range(1, vertices_coords.size()):
		aabb = aabb.expand(vertices_coords[i])
	
	var max_dimension = aabb.get_longest_axis_size()

	if max_dimension == 0:
		return 1.0

	return 1.0 / max_dimension
