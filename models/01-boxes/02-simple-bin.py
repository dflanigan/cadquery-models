
import cadquery as cq

from cadquery.vis import show, style

def make_bin(width: float, height:float) -> cq.Workplane:

    outside_fillet = width/10.0

    inside_width = width * 0.9
    inside_depth = height * 0.9

    shell = cq.Workplane("XY").box(width, width, height)

    cut = shell.faces(">Z").workplane().rect(inside_width, inside_width).extrude(-inside_depth,combine="cut")


    return cut

if __name__ == "__main__":

    print("Creating bin")

    result = make_bin(40.0, 20.0)

    print("Showing result")
    # show(result, alpha=0.5, gradient=False)
    show(style(result, color="blue", alpha=0.5), gradient=False)