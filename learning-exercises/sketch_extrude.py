import cadquery as cq 

length =80
width =50
thickness =8

def create_plate(length,width,thickness):

    return(cq.Workplane("XY").rect(length,width).extrude(thickness))

result = create_plate(length,width,thickness)

show_object(result)