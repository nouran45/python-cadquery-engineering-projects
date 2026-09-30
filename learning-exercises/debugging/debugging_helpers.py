import cadquery as cq

base = cq.Workplane("XY").box(40, 30, 6)
show_object(base, name="01_base")

top_face = base.faces(">Z")
show_object(top_face, name="02_top_face")

top_plane = top_face.workplane()

boss_profile = top_plane.circle(7)

with_boss = boss_profile.extrude(10)
show_object(with_boss, name="03_with_boss")

boss_top = with_boss.faces(">Z")

solid = boss_top.workplane().hole(5)
show_object(solid, name="04_final")