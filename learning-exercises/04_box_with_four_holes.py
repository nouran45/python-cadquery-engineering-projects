import cadquery as cq 

result = (cq.Workplane("XY").box(50,30,10).faces(">Z").workplane().pushPoints([(-20,-10),(-20,10),(20,-10),(20,10)]).hole(8))
#origin at x:25  y:15  offset is 5mm so subtract 5 
#pushpoints apply the hole to selected points at once 