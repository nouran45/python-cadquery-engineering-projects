import cadquery as cq


# ============================================================
# TASK 1 - STAGE 4
# Body + cavity + circular openings + rectangular openings
# ============================================================


# ============================================================
# MAIN DIMENSIONS
# ============================================================

W = 14.0       # long direction -> Y
H = 6.9        # short direction -> X
T = 1.0        # height -> Z


# ============================================================
# WALL / FLOOR DIMENSIONS
# ============================================================

wall_thickness = 0.20
floor_thickness = 0.20

outer_radius = 1.00
inner_radius = outer_radius - wall_thickness


# Inner dimensions
inner_H = H - 2 * wall_thickness
inner_W = W - 2 * wall_thickness


# ============================================================
# STAGE 1
# OUTER BODY
# ============================================================

outer = (
    cq.Workplane("XY")
    .box(
        H,                  # X = 6.9
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


# Cut cavity
solid = outer.cut(inner)


# ============================================================
# STAGE 3
# CIRCULAR OPENINGS
# ============================================================


# ------------------------------------------------------------
# CIRCLE 1
# Edge hole on +Y wall
# ------------------------------------------------------------

large_hole_diameter = 0.55
large_hole_radius = large_hole_diameter / 2

large_hole_x = -2.20
large_hole_z = 0.5775


# ------------------------------------------------------------
# CIRCLE 2
# Base/floor hole
# ------------------------------------------------------------

base_hole_diameter = 0.80
base_hole_radius = base_hole_diameter / 2

base_hole_x = -1.70
base_hole_y = 5.90


# ------------------------------------------------------------
# CUTTER SETTINGS
# ------------------------------------------------------------

hole_margin = 0.10
hole_cut_depth = 0.60


# ============================================================
# EDGE CIRCULAR HOLE
# +Y WALL
# ============================================================

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


solid = solid.cut(large_hole)


# ============================================================
# BASE CIRCULAR HOLE
# ============================================================

base_hole = (
    cq.Workplane(
        "XY",
        origin=(
            base_hole_x,
            base_hole_y,
            -0.05
        )
    )
    .circle(base_hole_radius)
    .extrude(floor_thickness + 0.10)
)


solid = solid.cut(base_hole)


# ============================================================
# STAGE 4
# RECTANGULAR OPENINGS
# ============================================================


# ============================================================
# RECTANGLE 1
# BIG ROUNDED RECTANGLE ON THE BASE
#
# Located at the +Y end and +X side
#
# X range approximately:
# 1.50 -> 2.70
#
# Y range approximately:
# 4.65 -> 6.35
# ============================================================

big_rect_width = 1.20       # X direction
big_rect_length = 1.70      # Y direction

big_rect_x = 2.10
big_rect_y = 5.50

big_rect_radius = 0.15


big_rect = (
    cq.Workplane(
        "XY",
        origin=(
            big_rect_x,
            big_rect_y,
            -0.05
        )
    )
    .box(
        big_rect_width,
        big_rect_length,
        floor_thickness + 0.10,
        centered=(True, True, False)
    )
    .edges("|Z")
    .fillet(big_rect_radius)
)


solid = solid.cut(big_rect)


# ============================================================
# RECTANGLE 2
# CENTER RECTANGLE ON BASE AT -Y END
#
# X range:
# -1.00 -> +1.00
#
# Y range:
# -5.80 -> -5.20
# ============================================================

bottom_rect_width = 2.00
bottom_rect_length = 0.60

bottom_rect_x = 0.00
bottom_rect_y = -5.50


bottom_rect = (
    cq.Workplane(
        "XY",
        origin=(
            bottom_rect_x,
            bottom_rect_y,
            -0.05
        )
    )
    .box(
        bottom_rect_width,
        bottom_rect_length,
        floor_thickness + 0.10,
        centered=(True, True, False)
    )
)


solid = solid.cut(bottom_rect)


# ============================================================
# RECTANGLE 3
# RECTANGULAR OPENING THROUGH -Y EDGE/WALL
#
# Shifted toward +X
#
# X range:
# 0.50 -> 1.40
#
# Z range:
# 0.2675 -> 0.7675
# ============================================================

edge_rect_width = 0.90
edge_rect_height = 0.50

edge_rect_x = 0.95
edge_rect_z = 0.5175


# -----------------
# Workplane for -Y wall
#
# Local horizontal = X
# Local vertical   = Z
# Cut direction    = +Y
# ------------

edge_rect_plane = cq.Plane(
    origin=(
        edge_rect_x,
        -W / 2 - hole_margin,
        edge_rect_z
    ),
    xDir=(1, 0, 0),
    normal=(0, 1, 0)
)


edge_rect = (
    cq.Workplane(edge_rect_plane)
    .rect(
        edge_rect_width,
        edge_rect_height
    )
    .extrude(hole_cut_depth)
)


solid = solid.cut(edge_rect)


#display
show_object(solid)