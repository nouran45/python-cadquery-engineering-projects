import cadquery as cq

length = 60
width = 40
thickness = 10

cy_diameter = 20
cy_height = 15


def create_box(length, width, thickness):
    return (
        cq.Workplane("XY")
        .box(length, width, thickness)
    )


def create_cylinder(part, cy_diameter, height):
    return (
        part
        .faces(">Z")
        .workplane()
        .circle(cy_diameter / 2)
        .extrude(height)
    )


box = create_box(length, width, thickness)

result = create_cylinder(box, cy_diameter, cy_height)

show_object(result)