import cadquery as cq

# Practice dimensions
W = 20
H = 10
T = 2

floor_thickness = 0.5
wall_thickness = 1.0
outer_radius = 1.5

inner_w = W - 2 * wall_thickness
inner_h = H - 2 * wall_thickness

cut_depth = T - floor_thickness
inner_radius = outer_radius - wall_thickness

# Stage 1: outer body
outer = (
    cq.Workplane("XY")
    .box(W, H, T)
    .edges("|Z")
    .fillet(outer_radius)
)

# Stage 2: rounded cavity cutter
inner = (
    cq.Workplane("XY")
    .box(inner_w, inner_h, cut_depth)
    .edges("|Z")
    .fillet(inner_radius)
    .translate((0, 0, floor_thickness / 2))
)

# Subtract cavity
solid = outer.cut(inner)

show_object(solid)