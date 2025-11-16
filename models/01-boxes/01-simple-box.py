
import cadquery as cq
from cadquery.vis import show


result = cq.Workplane("XY").box(6, 3, 0.5).edges("|Z").fillet(0.125)
show(result, alpha=0.5, edges=True, gradient=False)