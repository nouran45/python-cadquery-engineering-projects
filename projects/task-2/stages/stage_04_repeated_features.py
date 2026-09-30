import cadquery as cq


# ============================================================
# TASK 2 - STAGE 4 CORRECTED
# Stage 2 body unchanged
#
# TOP:
#   24 circular hollows
#
# BOTTOM:
#   recessed inner area
#   24 circular bosses inside the recess
#   bosses DO NOT extend below outer edge
# ============================================================


# ------------------------------------------------------------
# OVERALL DIMENSIONS
# ------------------------------------------------------------

W = 292.8
L = 427.8
T = 20.0


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
# CIRCULAR FEATURES
# ------------------------------------------------------------

feature_diameter = 54.0
feature_radius = feature_diameter / 2


# ------------------------------------------------------------
# TOP HOLLOWS
# ------------------------------------------------------------

hollow_diameter = 46.0
hollow_radius = hollow_diameter / 2

# top hollow depth
top_hollow_depth = 8.0


# ------------------------------------------------------------
# UNDERSIDE RECESSED AREA
# ------------------------------------------------------------

# Distance that the large underside field is pushed upward
bottom_recess_depth = 6.0

# Keep a border around the underside
bottom_border_width = 8.0

bottom_inner_W = main_W - 2 * bottom_border_width
bottom_inner_L = main_L - 2 * bottom_border_width

bottom_inner_radius = 8.0


# ------------------------------------------------------------
# 24 FEATURE POSITIONS
# ------------------------------------------------------------

x_positions = [
    -96.0,
    -32.0,
    32.0,
    96.0
]

y_positions = [
    -160.0,
    -96.0,
    -32.0,
    32.0,
    96.0,
    160.0
]


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
# STAGE 4A
# TOP CIRCULAR HOLLOWS
# ============================================================

for x in x_positions:
    for y in y_positions:

        top_hollow = (
            cq.Workplane("XY")
            .workplane(offset=T)
            .center(x, y)
            .circle(hollow_radius)
            .extrude(-top_hollow_depth)
        )

        solid = solid.cut(top_hollow)


# ============================================================
# STAGE 4B
# LARGE RECESSED UNDERSIDE AREA
# ============================================================

# This removes material from the underside inner area.
#
# Outer perimeter remains at Z = 0.
# Inner underside surface moves upward to Z = 6.

bottom_recess = (
    cq.Workplane("XY")
    .rect(
        bottom_inner_W,
        bottom_inner_L
    )
    .extrude(bottom_recess_depth)
    .edges("|Z")
    .fillet(bottom_inner_radius)
)


solid = solid.cut(bottom_recess)


# ============================================================
# STAGE 4C
# 24 BOTTOM CIRCULAR BOSSES
# ============================================================

# These start at the recessed underside surface:
#
# Z = 6
#
# and extend DOWN only to:
#
# Z = 0
#
# Therefore they DO NOT extend below the outer edge.

for x in x_positions:
    for y in y_positions:

        bottom_feature = (
            cq.Workplane("XY")
            .workplane(offset=bottom_recess_depth)
            .center(x, y)
            .circle(feature_radius)
            .extrude(-bottom_recess_depth)
        )

        solid = solid.union(bottom_feature)


# ------------------------------------------------------------
# DISPLAY
# ------------------------------------------------------------

show_object(solid)