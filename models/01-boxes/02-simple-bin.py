
import cadquery as cq
from cadquery.vis import show


def make_bin(width: float, height:float) -> cq.Workplane:

    outside_fillet = width/10.0
    shell = cq.Workplane("XY").box(width, width, height).edges("|Z").fillet(4.0)

    return shell

if __name__ == "__main__":

    print("Creating bin")

    result = make_bin(40.0, 20.0)

    print("Showing result")
    show(result)