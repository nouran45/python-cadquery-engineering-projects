import cadquery as cq

solid = (
    cq.Workplane("XY")
    .box(40, 30, 6)
    .faces(">Z")
    .workplane()
    .hole(8)
)

show_object(solid)

cq.exporters.export(
    solid,
    "practice_part.stl"
)