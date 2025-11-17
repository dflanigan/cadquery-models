
import cadquery as cq

from cadquery.vis import show, style

def make_cylinder_bin(height: float, radius:float, wall:float) -> cq.Workplane:

    inside_fillet = 2

    model = cq.Workplane("XY") \
        .cylinder(height=height, radius=radius) \
        .faces(">Z").workplane() \
        .circle(radius=(radius - wall)) \
        .cutBlind(until=-(height - wall)) \
        .faces("<Z[1]").edges().fillet(inside_fillet)

    return model

if __name__ == "__main__":

    print("Creating bin")

    result = make_cylinder_bin(height=60.0, radius=15.0, wall=3.0)

    print("Showing result")

    show(style(result, color="blue", alpha=0.5), gradient=False)
