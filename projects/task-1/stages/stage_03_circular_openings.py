import cadquery as cq


# ============================================================
# TASK 1 - STAGE 3
# Correct overall dimensions + cavity + 2 circular openings
# ============================================================


# ------------------------------------------------------------
# MAIN DIMENSIONS
# ------------------------------------------------------------

W = 14.0       # long direction -> Y
H = 6.9        # short direction -> X
T = 1.0        # total height -> Z


# ------------------------------------------------------------
# WALL / FLOOR DIMENSIONS
# ------------------------------------------------------------

wall_thickness = 0.20
floor_thickness = 0.20

outer_radius = 1.00
inner_radius = outer_radius - wall_thickness   # 0.80


# Inner dimensions
inner_H = H - 2 * wall_thickness
inner_W = W - 2 * wall_thickness


# ============================================================
# STAGE 1
# OUTER BODY
# ============================================================

outer = (
    cq.Workplane("XY")
    .box(H,                  # X = 6.9
        W,                  # Y = 14
        T,                  # Z = 1
        centered=(True, True, False)
    )
    .edges("|Z")
    .fillet(outer_radius)
)


# ============================================================
# STAGE 2
# INNER CAVITY
# ============================================================

# Make the cutter slightly taller than necessary so that
# the cavity definitely opens through the top.
cut_depth = T - floor_thickness + 0.02

inner = (
    cq.Workplane(
        "XY",
        origin=(0, 0, floor_thickness)
    )
    .box(
        inner_H,
        inner_W,
        cut_depth,
        centered=(True, True, False)
    )
    .edges("|Z")
    .fillet(inner_radius)
)


# Subtract cavity from outer body
solid = outer.cut(inner)


# ============================================================
# STAGE 3
# TWO CIRCULAR SIDE OPENINGS
# ============================================================


# ------------------------------------------------------------
# edge HOLE
# Located on the +Y end
# ------------------------------------------------------------

large_hole_diameter = 0.55
large_hole_radius = large_hole_diameter / 2

large_hole_x = -2.20
large_hole_z = 0.5775


# ------------------------------------------------------------
# base HOLE
# Located on the -X end
# ------------------------------------------------------------

base_hole_diameter = 0.8
base_hole_radius = base_hole_diameter / 2
base_hole_x = -1.7
base_hole_y = 5.9



# ------------------------------------------------------------
# CUTTER SETTINGS
# ------------------------------------------------------------

# Start slightly outside the object.
hole_margin = 0.10

# Long enough to pass completely through the wall
# and slightly into the empty cavity.
hole_cut_depth = 0.60


# ============================================================
# LARGE HOLE WORKPLANE
# ============================================================

# The large hole is on Y = +7.
#
# Start outside the model at Y = +7.1.
#
# normal = (0, -1, 0)
# means the cutter travels toward negative Y,
# therefore INTO the wall.

large_hole_plane = cq.Plane(
    origin=(
        large_hole_x,
        W / 2 + hole_margin,
        large_hole_z
    ),
    xDir=(1, 0, 0),
    normal=(0, -1, 0)
)


large_hole = (
    cq.Workplane(large_hole_plane)
    .circle(large_hole_radius)
    .extrude(hole_cut_depth)
)

# ============================================================
# CUT LARGE EDGE HOLE
# ============================================================

solid = solid.cut(large_hole)


# ============================================================
# BASE HOLE
# Hole through the flat floor
# ============================================================

base_hole = (
    cq.Workplane(
        "XY",
        origin=(base_hole_x, base_hole_y, -0.05)
    )
    .circle(base_hole_radius)
    .extrude(floor_thickness + 0.10)
)


# Cut base hole from the tray
solid = solid.cut(base_hole)


# ============================================================
# DISPLAY IN CQ-EDITOR
# ============================================================

show_object(solid)