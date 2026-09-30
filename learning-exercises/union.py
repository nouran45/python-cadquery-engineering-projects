import cadquery as cq


def create_box(length, width, height):
    return (
        cq.Workplane("XY")
        .box(length, width, height)
    )


def create_cylinder(diameter, height, z_position):
    return (
        cq.Workplane("XY")
        .workplane(offset=z_position)
        .circle(diameter / 2)
        .extrude(height)
    )


# Parameters
length = 50
width = 40
box_height = 20

cylinder_diameter = 20
cylinder_height = 15


# Create geometry
box = create_box(length, width, box_height)

cylinder = create_cylinder(
    cylinder_diameter,
    cylinder_height,
    box_height
)

# Combine them
result = box.union(cylinder)
show_object(result)