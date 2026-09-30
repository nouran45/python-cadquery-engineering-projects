import cadquery as cq

solid = (
    cq.Workplane("XY")
    .circle(10)
    .workplane(offset=20)
    .rect(12, 12)
    .loft()
)

show_object(solid)