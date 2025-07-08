@tool
extends MeshInstance3D

@export var directional_light: DirectionalLight3D

@export var regenerate_mesh: bool = false:
	set(value):
		if value:
			_generate_mesh()

var vertex_files = ["res://primitives/beatriz/vertex.csv", "res://primitives/julia/vertex.csv"]
var face_files = ["res://primitives/beatriz/face_vertices.csv", "res://primitives/julia/curved_face.csv"]

var colors_list = [Color.DODGER_BLUE, Color.ORANGE_RED]
var translations_list = [Vector3(0.8, 0, -1), Vector3(-0.2, 0, 0),]
var scale_list = [0.2, 0.2]

func _ready():
	_generate_mesh()

func _generate_mesh():
	const Colors = preload("res://scripts/rendering/colors.gd")
	const Primitives = preload("res://scripts/rendering/primitives.gd")
	const Deformer = preload("res://scripts/rendering/deformer.gd")

	var array_mesh = ArrayMesh.new()

	for i in range(vertex_files.size()):
		var st = SurfaceTool.new()
		st.begin(Mesh.PRIMITIVE_TRIANGLES)

		# CARREGA OS DADOS DOS VERTICES E FACES
		var vertex_data = Primitives.read_csv(vertex_files[i])
		var all_vertices = Primitives.extract_vertices(vertex_data)
		var face_data = Primitives.read_csv(face_files[i])
		var faces_with_coords = Primitives.extract_faces(all_vertices, face_data)[1]
		
		if i == 0:
			for face_verts in faces_with_coords:
				for j in range(1, face_verts.size() - 1):
					var v0 = face_verts[0] * scale_list[i] + translations_list[i]
					var v1 = face_verts[j] * scale_list[i] + translations_list[i]
					var v2 = face_verts[j+1] * scale_list[i] + translations_list[i]
					st.set_color(colors_list[i])
					st.add_vertex(v0); st.add_vertex(v1); st.add_vertex(v2)
		else:
			# IDENTIFICA O ÁPICE E A BASE DA PIRÂMIDE
			var all_vertex_coords = all_vertices[1]
			var apex = all_vertex_coords[0]
			for v in all_vertex_coords:
				if v.y > apex.y:
					apex = v

			var base_outline_original = faces_with_coords[0]

			# DEFORMAR A BASE DA PIRÂMIDE
			var curved_base_outline = Deformer.curve_pyramid_edges(base_outline_original, 0.7, 15)
			var base_center = Vector3.ZERO # Assumindo que o centro da base é a origem

			# CONSTRUIR AS FACES DA PIRÂMIDE
			for j in range(curved_base_outline.size()):
				var v0 = curved_base_outline[j]
				var v1 = curved_base_outline[(j + 1) % curved_base_outline.size()]

				var final_v0 = v0 * scale_list[i] + translations_list[i]
				var final_v1 = v1 * scale_list[i] + translations_list[i]
				var final_apex = apex * scale_list[i] + translations_list[i]
				
				st.set_color(colors_list[i])
				st.add_vertex(final_v0); st.add_vertex(final_v1); st.add_vertex(final_apex)

			# CONSTRUIR A BASE DA PIRÂMIDE
			for j in range(curved_base_outline.size()):
				var v0 = curved_base_outline[j]
				var v1 = curved_base_outline[(j + 1) % curved_base_outline.size()]

				var final_v0 = v0 * scale_list[i] + translations_list[i]
				var final_v1 = v1 * scale_list[i] + translations_list[i]
				var final_base_center = base_center * scale_list[i] + translations_list[i]

				st.set_color(colors_list[i])
				st.add_vertex(final_base_center); st.add_vertex(final_v1); st.add_vertex(final_v0)

		st.generate_normals()
		st.commit(array_mesh)
	
	self.mesh = array_mesh

	# CRIA A LUZ AMARELADA
	if is_instance_valid(directional_light):
		directional_light.light_color = Color.YELLOW
		directional_light.rotation_degrees = Vector3(-45, -60, 0)
		directional_light.light_energy = 1.5
		directional_light.shadow_enabled = true
		directional_light.light_angular_distance = 30

	# CRIA O EFEITO DE REFLEXÃO E MATERIAL POLIDO
	var polished_material = StandardMaterial3D.new()
	polished_material.shading_mode = StandardMaterial3D.SHADING_MODE_PER_PIXEL
	polished_material.vertex_color_use_as_albedo = true
	polished_material.metallic = 0.8
	polished_material.roughness = 0.4
	self.set_surface_override_material(0, polished_material)
	self.set_surface_override_material(1, polished_material)
