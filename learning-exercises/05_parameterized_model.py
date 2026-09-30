import cadquery as cq 

#parameters
length=50
width=30
height=10
thickness=25
hole_diameter=8
edge_offset=5

result = (cq.Workplane("XY").box(length,width,thickness).faces(">Z").workplane().pushPoints([
        (-(length / 2 - edge_offset), -(width / 2 - edge_offset)),
        (-(length / 2 - edge_offset),  (width / 2 - edge_offset)),
        ( (length / 2 - edge_offset), -(width / 2 - edge_offset)),
        ( (length / 2 - edge_offset),  (width / 2 - edge_offset))
    ]).hole(hole_diameter))