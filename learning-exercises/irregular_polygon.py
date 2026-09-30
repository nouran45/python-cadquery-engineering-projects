import cadquery as cq

points = [
    (0, 0),
    (30, 0),
    (30, 15),
    (22, 15),
    (16, 10),
    (8, 10),
    (8, 5),
    (0, 5)
]

solid = (
    cq.Workplane("XY")
    .polyline(points)
    .close()
    .extrude(4)
)

show_object(solid)