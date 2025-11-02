
import cadquery as cq
from cadquery.vis import show

if __name__ == "__main__":

    result = cq.Workplane("XY").box(3, 3, 0.5).edges("|Z").fillet(0.125)
    show(result)