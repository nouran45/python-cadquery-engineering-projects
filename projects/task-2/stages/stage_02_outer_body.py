import cadquery as cq


# ============================================================
# TASK 2 - STAGE 2
# Main body + stepped / beveled outer profile
# ============================================================


# ------------------------------------------------------------
# OVERALL DIMENSIONS
# ------------------------------------------------------------

W = 292.8          # overall X width
L = 427.8          # overall Y length
T = 20.0           # total height


# ------------------------------------------------------------
# LOWER BASE / EDGE
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
# MAIN NARROWER BODY
# ============================================================

main_body = (
    cq.Workplane("XY")
    .workplane(offset=base_height)
    .rect(main_W, main_L)
    .extrude(main_height)
    .edges("|Z")
    .fillet(main_corner_radius)
)


# ------------------------------------------------------------
# COMBINE BOTH PARTS
# ------------------------------------------------------------

solid = bottom_base.union(main_body)


# ------------------------------------------------------------
# DISPLAY
# ------------------------------------------------------------

show_object(solid)