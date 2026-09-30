import cadquery as cq

solid = (
    cq.Workplane("XY")
    .box(30, 20, 4)
    .edges("|Z")
    .fillet(3)
)

show_object(solid)