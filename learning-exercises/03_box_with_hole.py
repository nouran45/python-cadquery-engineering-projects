import cadquery as cq

result = (cq.Workplane("XY").box(50,30,10).faces(">Z").workplane().hole(8))
# the 8 in hole is a diameter not radius 