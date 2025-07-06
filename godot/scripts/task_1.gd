@tool
extends MeshInstance3D

@export var regenerate_mesh: bool = false:
	set(value):
		if value:
			_generate_mesh()

var vertex_file: String = "res://primitives/julia/vertex.csv"
var edge_file: String = "res://primitives/julia/edge.csv"

func _ready():
	_generate_mesh()

func _generate_mesh():
	const Primitives = preload("res://scripts/rendering/primitives.gd")

	var vertex_data = Primitives.read_csv(vertex_file)
	var vertices_list = Primitives.extract_vertices(vertex_data)
	
	var scale_factor = Primitives.get_normalization_scale_factor(vertices_list[1]) * 2
		
	var edge_data = Primitives.read_csv(edge_file)
	var edges_list = Primitives.extract_edges(vertices_list, edge_data)

	var immediate_mesh = ImmediateMesh.new()
	immediate_mesh.surface_begin(Mesh.PRIMITIVE_LINES)

	for edge in edges_list[1]:
		immediate_mesh.surface_add_vertex(edge[0] * scale_factor)
		immediate_mesh.surface_add_vertex(edge[1] * scale_factor)
	
	immediate_mesh.surface_end()
	self.mesh = immediate_mesh

	var standard_material = StandardMaterial3D.new()
	standard_material.albedo_color = Color.PURPLE
	standard_material.shading_mode = StandardMaterial3D.SHADING_MODE_UNSHADED
	self.material_override = standard_material
