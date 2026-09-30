import cadquery as cq

#base parameters
b_length=60
b_width=40
b_height=10

#raised rect param
raised_length=30
raised_width=20
raised_height=8

#circular hole param
circle_diameter=10
circle_depth=18
#cut rect param
cut_length=20
cut_width=5


def create_base():
    return (cq.Workplane("XY")
        .box(b_length,b_width,b_height))

def create_raised_rect(base):
    return(base
        .faces(">Z")    
        .workplane()
        .rect(raised_length,raised_width)
        .extrude(raised_height))

def create_circular_hole(part):
    return(part
        .faces(">Z")
        .workplane()
        .hole(circle_diameter,circle_depth))

def rectangular_side_cut(part, depth=15):
    return (
        part
        .faces("<Y")
        .workplane(centerOption="CenterOfMass")   # fix 1: center on the actual face
        .rect(cut_length, cut_width)
        .cutBlind(-depth)                          # fix 2: negative = cut inward
    )

#build model

base=create_base()
raisedRect=create_raised_rect(base)
hole=create_circular_hole(raisedRect)
rectCut=rectangular_side_cut(hole)

result=rectCut

show_object(result)