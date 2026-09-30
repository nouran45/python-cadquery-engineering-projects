import cadquery as cq

solid = (
    cq.Workplane("XY")
    .box(30, 20, 5)
    .faces(">Z")
    .workplane()
    .center(7,4)
    .circle(6)
    .extrude(8)
    .faces(">Z")
    .workplane()
    .hole(4)
)

show_object(solid)