
import cadquery as cq
from cadquery.vis import show, style

def make_cylinder(radius:float, height: float) -> cq.Workplane:

    result = cq.Workplane("XY").cylinder(height=height, radius=radius)

    return result

def side_shell(shape, thickness: float) -> cq.Workplane:

    shell = shape.faces("+Z or -Z").shell(thickness)

    return shell

cylinder = make_cylinder(radius=20, height=60)

cylinder_shell = side_shell(cylinder, 1.0)

show(style(cylinder, color="blue", alpha=0.5), style(cylinder_shell, color="red", alpha=0.25), gradient=False)