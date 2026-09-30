import cadquery as cq

solid = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(20, 0)
    .lineTo(20, 5)
    .lineTo(5, 5)
    .lineTo(5, 20)
    .lineTo(0, 20)
    .close()
    .extrude(5)
)

show_object(solid)