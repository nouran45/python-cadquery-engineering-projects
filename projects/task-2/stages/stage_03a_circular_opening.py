import cadquery as cq


# ============================================================
# TASK 2 - STAGE 3
# Main body + ONE circular opening
# ============================================================


# ------------------------------------------------------------
# OVERALL DIMENSIONS
# ------------------------------------------------------------

W = 292.8          # X direction
L = 427.8          # Y direction
T = 20.0           # total Z height


# ------------------------------------------------------------
# LOWER BASE
# ------------------------------------------------------------

base_height = 2.0

base_corner_radius = 16.0


# ------------------------------------------------------------
# MAIN UPPER BODY
# ------------------------------------------------------------

main_W = 268.4
main_L = 409.2

main_height = T - base_height

main_corner_radius = 12.0


# ------------------------------------------------------------
# CIRCULAR FEATURE DIMENSIONS
# ------------------------------------------------------------

hole_diameter = 48.0
hole_radius = hole_diameter / 2

# Slightly larger surrounding diameter
rim_diameter = 52.0
rim_radius = rim_diameter / 2

# Position of ONE test opening
circle_x = -96.0
circle_y = -160.0


# ============================================================
# STAGE 1
# LOWER WIDE BASE
# ============================================================

bottom_base = (
    cq.Workplane("XY")
    .rect(W, L)
    .extrude(base_height)
    .edges("|Z")
    .fillet(base_corner_radius)
)


# ============================================================
# STAGE 2
# MAIN BODY
# ============================================================

main_body = (
    cq.Workplane("XY")
    .workplane(offset=base_height)
    .rect(main_W, main_L)
    .extrude(main_height)
    .edges("|Z")
    .fillet(main_corner_radius)
)


# Combine the body
solid = bottom_base.union(main_body)


# ============================================================
# STAGE 3A
# ONE THROUGH CIRCULAR OPENING
# ============================================================

hole = (
    cq.Workplane("XY")
    .center(circle_x, circle_y)
    .circle(hole_radius)
    .extrude(T)
)


# Cut the opening from the body
solid = solid.cut(hole)


# ============================================================
# DISPLAY
# ============================================================

show_object(solid)