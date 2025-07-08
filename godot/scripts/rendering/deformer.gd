class_name Deformer
extends RefCounted

static func _generate_quadratic_bezier_curve(p0: Vector3, p1: Vector3, p2: Vector3, num_points: int) -> PackedVector3Array:
	var points = PackedVector3Array()
	if num_points <= 1:
		points.push_back(p0)
		return points
	for i in range(num_points):
		var t = float(i) / (num_points - 1)
		var q0 = p0.lerp(p1, t)
		var q1 = p1.lerp(p2, t)
		var r = q0.lerp(q1, t)
		points.push_back(r)
	return points

static func curve_pyramid_edges(face_vertices: PackedVector3Array, curve_factor: float = 0.4, num_points_per_edge: int = 10) -> PackedVector3Array:
	if face_vertices.size() < 3:
		return face_vertices

	var new_outline_points = PackedVector3Array()

	var face_centroid = Vector3.ZERO
	for v in face_vertices:
		face_centroid += v
	face_centroid /= face_vertices.size()
	
	for i in range(face_vertices.size()):
		var p0 = face_vertices[i]
		var p2 = face_vertices[(i + 1) % face_vertices.size()]
		
		var midpoint = (p0 + p2) / 2.0
		var control_point = midpoint.lerp(face_centroid, curve_factor)

		var edge_points = _generate_quadratic_bezier_curve(p0, control_point, p2, num_points_per_edge)
		edge_points.resize(edge_points.size() - 1)
		
		new_outline_points.append_array(edge_points)

	return new_outline_points
