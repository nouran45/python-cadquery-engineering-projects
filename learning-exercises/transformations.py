#========
#translate
#========
"""
import cadquery as cq

part = cq.Workplane("XY").box(20, 10, 5)

moved = part.translate((0, -20, 30))

show_object(moved)
"""
#=========
#Rotate
#=========
"""
import cadquery as cq

part = cq.Workplane("XY").box(30, 8, 4)

solid = part.rotate(
    (0, 0, 0),#axis start
    (0, 0, 1),#define the z direction
    45 #45 degree around z axis
)

show_object(solid)
"""
#========
#Mirror
#========
"""
import cadquery as cq

half = (
    cq.Workplane("XY")
    .box(20, 8, 5)
    .translate((8, 0, 0))
)

other_half = half.mirror("YZ")

solid = half.union(other_half)
"""


show_object(solid)
