@tool
extends MeshInstance3D

@export var regenerate_mesh: bool = false:
	set(value):
		if value:
			_generate_mesh()

var vertex_files = ["res://primitives/beatriz/vertex.csv", "res://primitives/julia/vertex.csv"]
var face_files = ["res://primitives/beatriz/face_vertices.csv", "res://primitives/julia/face_vertices.csv"]

var colors_list = [Color.GREEN, Color.BLUE]
var distance_list = [Vector3(0.8, 0, -1.2), Vector3(0, 0, 0)]
var scale_list = [0.2, 0.2]

func _ready():
	_generate_mesh()

func _generate_mesh():
	const Primitives = preload("res://scripts/rendering/primitives.gd")

	var immediate_mesh = ImmediateMesh.new()
	immediate_mesh.surface_begin(Mesh.PRIMITIVE_TRIANGLES)

	for i in range(vertex_files.size()):
		var vertex_file = vertex_files[i]
		var vertex_data = Primitives.read_csv(vertex_file)
		var vertices = Primitives.extract_vertices(vertex_data)

		var face_data = Primitives.read_csv(face_files[i])
		var faces = Primitives.extract_faces(vertices, face_data)[1]

		var current_color = colors_list[i]
		var translation = distance_list[i]
		
		for face_vertices in faces:
			if face_vertices.size() >= 3:
				var v0 = face_vertices[0]
				for j in range(1, face_vertices.size() - 1):
					var v1 = face_vertices[j]
					var v2 = face_vertices[j+1]
					
					var normal = (v1 - v0).cross(v2 - v0).normalized()
					immediate_mesh.surface_set_normal(normal)
					
					immediate_mesh.surface_set_color(current_color)
					immediate_mesh.surface_add_vertex(v0 * scale_list[i] + translation)
					immediate_mesh.surface_add_vertex(v1 * scale_list[i] + translation)
					immediate_mesh.surface_add_vertex(v2 * scale_list[i] + translation)
	
	immediate_mesh.surface_end()
	self.mesh = immediate_mesh

	var standard_material = StandardMaterial3D.new()
	standard_material.vertex_color_use_as_albedo = true
	standard_material.shading_mode = StandardMaterial3D.SHADING_MODE_PER_PIXEL
	self.material_override = standard_material
