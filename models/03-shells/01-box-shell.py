
import cadquery as cq
from cadquery.vis import show, style

def box_shell(width: float, height: float, outside_fillet: float) -> cq.Workplane:

    result = cq.Workplane("XY").box(width, width, height).edges("|Z").fillet(outside_fillet)

    return result

def side_shell(shape, thickness: float) -> cq.Workplane:

    shell = shape.faces("+Z or -Z").shell(thickness)

    return shell



box = box_shell(40, 30, 4)

box_shell = side_shell(box, 1.0)

show(style(box_shell, color="blue", alpha=0.5), style(box, color="red", alpha=0.25), gradient=False)