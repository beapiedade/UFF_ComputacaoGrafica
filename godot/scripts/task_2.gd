@tool
extends MeshInstance3D

@export var label_node_path: NodePath

@export var regenerate_in_editor: bool = false:
	set(value):
		if value:
			_load_data_and_generate_mesh()

# Task 2: Alternate Colors Projection
var vertex_file: String = "res://primitives/julia/vertex.csv"
var face_file: String = "res://primitives/beatriz/face_vertices.csv"

var faces_list = []
var scale_factor = 1.0

var colors_list = []
var colors_time_gap = 500
var colors_time_stamp = 0
var is_data_loaded = false

func _ready():
	if Engine.is_editor_hint():
		return
		
	_load_data_and_generate_mesh()
	colors_time_stamp = Time.get_ticks_msec()

func _process(_delta):
	if Engine.is_editor_hint():
		return

	var current_time = Time.get_ticks_msec()
	if current_time - colors_time_stamp > colors_time_gap:
		if not colors_list.is_empty():
			colors_list.push_back(colors_list.pop_front())
			_generate_mesh()
			colors_time_stamp = current_time

	if not label_node_path.is_empty():
		var label_node = get_node_or_null(label_node_path)
		if label_node:
			label_node.text = "Tempo: %.1f s" % (Time.get_ticks_msec() / 1000.0)

func _load_data_and_generate_mesh():
	_load_data_from_files()
	_generate_mesh()

func _load_data_from_files():	
	const Primitives = preload("res://scripts/rendering/primitives.gd")
	const Colors = preload("res://scripts/rendering/colors.gd")
	
	var vertex_data = Primitives.read_csv(vertex_file)
	var vertices_list = Primitives.extract_vertices(vertex_data)
	
	scale_factor = Primitives.get_normalization_scale_factor(vertices_list[1]) * 2
	
	var faces_data = Primitives.read_csv(face_file)
	faces_list = Primitives.extract_faces(vertices_list, faces_data)
	
	if not faces_list.is_empty():
		var hsv_colors = Colors.generate_hsv(faces_list[1].size())
		colors_list = Colors.to_rgb(hsv_colors)
	
	is_data_loaded = true

func _generate_mesh():
	var immediate_mesh = ImmediateMesh.new()
	immediate_mesh.surface_begin(Mesh.PRIMITIVE_TRIANGLES)

	var faces = faces_list[1]
	for i in range(faces.size()):
		var face_vertices = faces[i]
		immediate_mesh.surface_set_color(colors_list[i])
		
		if face_vertices.size() >= 3:
			var v0 = face_vertices[0]
			for j in range(1, face_vertices.size() - 1):
				immediate_mesh.surface_add_vertex(v0 * scale_factor)
				immediate_mesh.surface_add_vertex(face_vertices[j] * scale_factor)
				immediate_mesh.surface_add_vertex(face_vertices[j+1] * scale_factor)
	
	immediate_mesh.surface_end()
	self.mesh = immediate_mesh

	var standard_material = StandardMaterial3D.new()
	standard_material.vertex_color_use_as_albedo = true
	standard_material.shading_mode = StandardMaterial3D.SHADING_MODE_UNSHADED
	self.material_override = standard_material
