import cadquery as cq


# ============================================================
# MAIN PARAMETERS
# ============================================================

w = 15
h = 50


# ============================================================
# LOWER CYLINDER
# ============================================================

base_circle_r = w * 0.64
base_height = h * 1.20


# ============================================================
# MIDDLE FLANGE
# ============================================================

mid_circle_r = w * 1.04
mid_height = h * 0.03



# UPPER HEAD


top_circle_r = w * 1.20
top_height = h * 0.50

# Outer circular top fillet
top_fillet_r = w * 0.16


# ============================================================
# HEXAGONAL OPENING
# ============================================================

cutter_sides = 6
cutter_radius = w * 1.80

# Final top Z of the model
model_top_z = (
    base_height
    + mid_height
    + top_height
)

# Cutter starts slightly above the model
cutter_origin_z = model_top_z + 1

# Cut downward through most of the head
cutter_extrude = -(top_height - 1)


# ------------------------------------------------------------
# FILLET OF THE HEXAGONAL LIP
# ------------------------------------------------------------



hex_lip_fillet_r = w * 0.12


# ============================================================
# CREATE MAIN SOLID
# ============================================================

solid = (
    cq.Workplane("XY")

    # Lower cylinder
    .circle(base_circle_r)
    .extrude(base_height)

    # Middle flange
    .faces(">Z")
    .circle(mid_circle_r)
    .extrude(mid_height)

    # Large upper head
    .faces(">Z")
    .circle(top_circle_r)
    .extrude(top_height)

    # Round outer circular top edge
    .faces(">Z")
    .fillet(top_fillet_r)
)


# ============================================================
# CREATE HEXAGON CUTTER
# ============================================================


# First create the actual hexagonal cavity.

cutter = (
    cq.Workplane(
        "XY",
        origin=(0, 0, cutter_origin_z)
    )
    .polygon(
        cutter_sides,
        cutter_radius
    )
    .extrude(cutter_extrude)
)


# ============================================================
# CUT THE HEXAGONAL SOCKET
# ============================================================

solid = solid.cut(cutter)


# ============================================================
# FILLET THE FINISHED HEXAGONAL OPENING
# ============================================================

# Select the top face.
#
# The outer head edge is circular.
# The six opening edges are straight LINE edges.
#
# Therefore %LINE isolates the six edges around the hex opening.

solid = (
    solid
    .faces(">Z")
    .edges("%LINE")
    .fillet(hex_lip_fillet_r)
)


# ============================================================
# DISPLAY
# ============================================================

show_object(solid)


# ============================================================
# EXPORT
# ============================================================

cq.exporters.export(
    solid,
    "Task2_After.stl"
)