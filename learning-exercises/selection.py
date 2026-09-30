import cadquery as cq


length = 50
width = 40
height = 20

cylinder_diameter = 20
boss_height = 5


result = (
    cq.Workplane("XY")
    .box(length, width, height)
    .faces(">Z")
    .workplane()
    .circle(cylinder_diameter / 2)
    .extrude(boss_height)
)
