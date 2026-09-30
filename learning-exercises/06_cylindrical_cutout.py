import cadquery as cq

length=50
width=40
thickness=20
cylinder_diameter=20

def create_box(length, width, thickness):
    return (
        cq.Workplane("XY")
        .box(length, width, thickness)
    )


def create_cylinder(diameter, height):
    return (
        cq.Workplane("XY")
        .circle(diameter / 2)
        .extrude(height)
    )

box=create_box(length,width,thickness)
cylinder=create_cylinder(cylinder_diameter,thickness)



result = box.cut(cylinder)

show_object(result)