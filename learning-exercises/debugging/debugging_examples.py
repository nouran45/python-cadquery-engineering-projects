#======
#debug1
#======
"""
import cadquery as cq

solid = (
    cq.Workplane("XY")
    .moveTo(0, 0)
    .lineTo(30, 0)
    .lineTo(30, 20)
    .lineTo(0, 20)
    .extrude(5)
)

You drew:

A → B → C → D

but never:

D → A

The profile isn't closed.

add close() before extrude 

show_object(solid)
"""

#======
#debug2
#======
"""
import cadquery as cq

solid = (
    cq.Workplane("XY")
    .box(30, 20, 5)
    .faces(">Z")
    .workplane()
    .center(100, 0)
    .circle(3)
    .cutThruAll()
)

show_object(solid)

where did you put the hole?

100 units away

possibly completely outside the part.
"""
#=====
#debug3
#=====
import cadquery as cq

solid = cq.Workplane("XY").box(40, 30, 10)

bb = solid.val().BoundingBox()

print("X:", bb.xlen)
print("Y:", bb.ylen)
print("Z:", bb.zlen)

show_object(solid)