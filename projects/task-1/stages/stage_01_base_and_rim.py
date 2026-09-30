import cadquery as cq

# Required overall dimensions from the assignment
W = 14.0
H = 6.9
T = 1.0

# YOU choose these after looking at the STL/reference
floor_thickness = 1
wall_thickness = 1
outer_radius = 1

# Derived values
inner_w = W - 2 * wall_thickness
inner_h = H - 2 * wall_thickness

# 1) Create complete outer block
solid = cq.Workplane("XY").box(W, H, T)

# 2) Round the four outer vertical corners
solid = (
    solid
    .edges("|Z")
    .fillet(outer_radius)
)

# 3) Select top face
top = solid.faces(">Z").workplane()

# 4) Define the cavity profile
# You will need to decide how to make this rounded,
# rather than leaving it as a sharp rectangle.
cavity = (
    top
    .rect(inner_w, inner_h)
)

# 5) Remove material downward while leaving the floor
cut_depth = T - floor_thickness

# Continue here with the appropriate blind cut
# after deciding the direction/sign in CQ-editor.

show_object(solid)