import cadquery as cq

part = cq.Workplane("XY").box(40, 30, 6)
show_object(part, name="01_base")

top = part.faces(">Z")

selection = part.faces(">Z").edges("|Z")

print(selection.size())

show_object(top)