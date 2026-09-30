import cadquery as cq

solid = (
    cq.Workplane("XY")
    .box(40, 30, 20)
    .faces(">Z")
    .shell(-5)
)

show_object(solid)