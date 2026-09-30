import cadquery as cq
import math


# ============================================================
# TASK 2 - STAGE 5 REFINED
# Add bigger outlined stars inside the top hollows
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
top_hollow_depth = 8.0

# floor of each top hollow
hollow_floor_z = T - top_hollow_depth


# ------------------------------------------------------------
# UNDERSIDE RECESSED AREA
# ------------------------------------------------------------

bottom_recess_depth = 6.0
bottom_border_width = 8.0

bottom_inner_W = main_W - 2 * bottom_border_width
bottom_inner_L = main_L - 2 * bottom_border_width

bottom_inner_radius = 8.0


# ------------------------------------------------------------
# STAR DIMENSIONS (REFINED)
# ------------------------------------------------------------

# Bigger outer star
star_outer_radius = 12.0
star_inner_radius = 5.2

# Smaller inner star that stays flat (not extruded)
inner_star_outer_radius = 7.0
inner_star_inner_radius = 3.0

# shallow extrusion height for the border only
star_height = 1.5


# ------------------------------------------------------------
# ALL 24 FEATURE POSITIONS
# ------------------------------------------------------------

x_positions = [-96.0, -32.0, 32.0, 96.0]
y_positions = [-160.0, -96.0, -32.0, 32.0, 96.0, 160.0]


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
# COMBINE BODY
# ------------------------------------------------------------

solid = bottom_base.union(main_body)


# ============================================================
# STAGE 4A
# 24 TOP CIRCULAR HOLLOWS
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

bottom_recess = (
    cq.Workplane("XY")
    .rect(bottom_inner_W, bottom_inner_L)
    .extrude(bottom_recess_depth)
    .edges("|Z")
    .fillet(bottom_inner_radius)
)

solid = solid.cut(bottom_recess)


# ============================================================
# STAGE 4C
# 24 UNDERSIDE CIRCULAR BOSSES
# ============================================================

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


# ============================================================
# HELPER FUNCTION
# CREATE STAR POINTS
# ============================================================

def make_star_points(cx, cy, outer_r, inner_r):
    points = []
    start_angle = 90.0

    for i in range(10):
        angle_deg = start_angle + i * 36.0
        angle_rad = math.radians(angle_deg)

        if i % 2 == 0:
            radius = outer_r
        else:
            radius = inner_r

        px = cx + radius * math.cos(angle_rad)
        py = cy + radius * math.sin(angle_rad)
        points.append((px, py))

    return points


# ============================================================
# STAGE 5
# 
# ============================================================

for x in x_positions:
    for y in y_positions:

        # Outer bigger star
        outer_star_points = make_star_points(
            x, y,
            star_outer_radius,
            star_inner_radius
        )

        # Inner smaller star
        inner_star_points = make_star_points(
            x, y,
            inner_star_outer_radius,
            inner_star_inner_radius
        )

        # Create extruded outer star
        outer_star = (
            cq.Workplane("XY")
            .workplane(offset=hollow_floor_z)
            .polyline(outer_star_points)
            .close()
            .extrude(star_height)
        )

        # Create inner star cutter
        inner_star_cut = (
            cq.Workplane("XY")
            .workplane(offset=hollow_floor_z)
            .polyline(inner_star_points)
            .close()
            .extrude(star_height)
        )

        # Keep only the star border/outline
        star_border = outer_star.cut(inner_star_cut)

        # Add to solid
        solid = solid.union(star_border)


# ------------------------------------------------------------
# DISPLAY
# ------------------------------------------------------------

show_object(solid)

# ------------------------------------------------------------
# EXPORT FINAL MODEL
# ------------------------------------------------------------

cq.exporters.export(solid, "Task2.stl")