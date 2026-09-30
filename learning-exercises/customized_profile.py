import cadquery as cq 

overall_length = 80
overall_height = 60

upper_length = 60
step_height = 20

profile_thickness = 20
extrude_height = 10

def create_profile(overall_length, overall_height,
                   upper_length, profile_thickness,
                   extrude_height):

    return (
        cq.Workplane("XY")
        .moveTo(0, 0)
        .lineTo(overall_length, 0)
        .lineTo(overall_length, profile_thickness)
        .lineTo(upper_length, profile_thickness)
        .lineTo(upper_length, overall_height)
        .lineTo(0, overall_height)
        .close()
        .extrude(extrude_height)
    )


result = create_profile(overall_length, overall_height,
                   upper_length, profile_thickness,
                   extrude_height)
show_object(result)