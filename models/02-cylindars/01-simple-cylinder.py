
import cadquery as cq
from cadquery.vis import show, style


result = cq.Workplane("XY").cylinder(height=60.0, radius=15.0)
show(style(result, color="blue", alpha=0.5), gradient=False)