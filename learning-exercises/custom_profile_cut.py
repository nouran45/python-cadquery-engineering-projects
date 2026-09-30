import cadquery as cq


# =========================
# Parameters
# =========================

length = 80
width = 50
plate_height = 10

slot_length = 40
slot_width = 15
slot_depth = 5


# =========================
# Create plate
# =========================

def create_plate(length, width, height):
    return (
        cq.Workplane("XY")
        .rect(length, width)
        .extrude(height)
    )


# =========================================
# Method 1: faces(">Z")
# =========================================

def create_slot_with_face(part, slot_length, slot_width, slot_depth):
    return (
        part
        .faces(">Z")
        .workplane()
        .rect(slot_length, slot_width)
        .cutBlind(-slot_depth)
    )


# =========================================
# Method 2: workplane(offset=...)
# =========================================

def create_slot_with_offset(
    slot_length,
    slot_width,
    slot_depth,
    plate_height
):
    return (
        cq.Workplane("XY")
        .workplane(offset=plate_height)
        .rect(slot_length, slot_width)
        .extrude(-slot_depth)
    )


# =========================
# Create two plates
# =========================

plate1 = create_plate(
    length,
    width,
    plate_height
)

plate2 = create_plate(
    length,
    width,
    plate_height
)


# =========================
# Method 1
# =========================

result_face = create_slot_with_face(
    plate1,
    slot_length,
    slot_width,
    slot_depth
)


# =========================
# Method 2
# =========================

slot = create_slot_with_offset(
    slot_length,
    slot_width,
    slot_depth,
    plate_height
)

result_offset = plate2.cut(slot)


# Move Method 2 to the right
result_offset = result_offset.translate((100, 0, 0))


# =========================
# Show both
# =========================

show_object(result_face, name="faces >Z")

show_object(result_offset, name="offset")