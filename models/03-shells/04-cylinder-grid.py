
import cadquery as cq
from cadquery import Workplane
from cadquery.vis import show, style

def make_cylinder(radius: float, height: float) -> cq.Workplane:

    result = cq.Workplane("XY").cylinder(height=height, radius=radius)

    return result

def side_shell(shape, thickness: float) -> cq.Workplane:

    shell = shape.faces("+Z or -Z").shell(thickness)

    return shell

def add_plane_pattern(shell) -> cq.Workplane:

    grid = Workplane("XY")

    spacing = 5.1
    thickness = 0.25

    r_start = -7
    r_end = 7

    for z in range(r_start, r_end):
        plane = cq.Workplane("XY").box(100.0, 100.0, thickness)
        grid = grid.add(plane.translate((0.0,0.0,z * spacing)))

    for y in range(r_start, r_end):
        plane = cq.Workplane("XY").box(100.0, thickness, 100.0)
        grid = grid.add(plane.translate((0.0, y * spacing , 0.0)))

    for x in range(r_start, r_end):
        plane = cq.Workplane("XY").box(thickness, 100.0, 100.0)
        grid = grid.add(plane.translate((x * spacing, 0.0 , 0.0)))

    rotated_plane = grid.rotateAboutCenter((1.0, 1.0, 1.0), 30.0)

    pattern = rotated_plane.intersect(shell)

    return pattern


cylinder = make_cylinder(25, 60)
cylinder_shell = side_shell(cylinder, 0.5)

cylinder_texture = add_plane_pattern(cylinder_shell)

show(style(cylinder_texture, color="blue"), style(cylinder, color="red"), gradient=False)