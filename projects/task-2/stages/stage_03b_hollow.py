import cadquery as cq


# ============================================================
# TASK 2 - STAGE 3B
# Keep Stage 3A body exactly
# Add ONE bottom hollow under the circular feature
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


# ------------------------------------------------------------
# TOP CIRCULAR FEATURE
# ------------------------------------------------------------

feature_diameter = 54.0
feature_radius = feature_diameter / 2
feature_height = 10.0


# ------------------------------------------------------------
# BOTTOM HOLLOW
# ------------------------------------------------------------

# Slightly smaller than the top feature
hollow_diameter = 46.0
hollow_radius = hollow_diameter / 2

# Blind depth from the bottom upward
hollow_depth = 14.0


# ------------------------------------------------------------
# ONE TEST FEATURE POSITION
# ------------------------------------------------------------

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
# COMBINE STAGE 1 + STAGE 2
# ------------------------------------------------------------

solid = bottom_base.union(main_body)


# ============================================================
# STAGE 3A
# ONE WIDER + HIGHER CIRCULAR FEATURE
# ============================================================

feature = (
    cq.Workplane("XY")
    .workplane(offset=T)
    .center(circle_x, circle_y)
    .circle(feature_radius)
    .extrude(feature_height)
)

solid = solid.union(feature)


# ============================================================
# STAGE 3B
# ONE BOTTOM HOLLOW (BLIND, NOT THROUGH)
# ============================================================

bottom_hollow = (
    cq.Workplane("XY")
    .center(circle_x, circle_y)
    .circle(hollow_radius)
    .extrude(hollow_depth)
)

solid = solid.cut(bottom_hollow)


# ------------------------------------------------------------
# DISPLAY
# ------------------------------------------------------------

show_object(solid)