
import cadquery as cq
from cadquery.vis import show, style

def box_shell(width: float, height: float, outside_fillet: float) -> cq.Workplane:

    result = cq.Workplane("XY").box(width, width, height).edges("|Z").fillet(outside_fillet)

    return result

def side_shell(shape, thickness: float) -> cq.Workplane:

    shell = shape.faces("+Z or -Z").shell(thickness)

    return shell


def test_piece(width: float, height:float, wall:float = 4):

    straight_piece = (
        cq.Sketch()
        .segment((0.0,0.0), (wall, 0.0))
        .segment((wall, 0.0), (wall, width))
        .segment((wall, width), (0.0, width))
        .close()
        .assemble()
    )

    h_width = width/2.0

    curve_piece = (
        cq.Sketch()
        .arc((wall, 0.0),(wall+h_width, h_width),(wall, width))
        .segment((wall, width),(wall, width-wall))
        .arc((wall, width-wall),(h_width, h_width),(wall,wall))
        .close()
        .assemble()
    )

    full_piece  = cq.Workplane("XY").placeSketch(straight_piece + curve_piece).extrude(height)

    return full_piece





test_1 = test_piece(60, 40)


show(style(test_1, color="red", alpha=0.25), gradient=False)

#show(style(box_shell, color="blue", alpha=0.5), style(box, color="red", alpha=0.25), gradient=False)