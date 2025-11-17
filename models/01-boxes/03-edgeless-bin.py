
import cadquery as cq

from cadquery.vis import show, style

def make_bin(width: float, height:float, wall:float) -> cq.Workplane:

    outside_fillet = wall + 2
    inside_fillet = 2

    model = cq.Workplane("XY") \
        .box(width, width, height) \
        .edges('|Z').fillet(outside_fillet) \
        .faces(">Z").workplane() \
        .rect(width - (2 * wall), width - (2 * wall)) \
        .cutBlind(until=-(height - wall)) \
        .edges("|Z").fillet(inside_fillet) \
        .faces("<Z[1]").edges().fillet(inside_fillet)

    return model

if __name__ == "__main__":

    print("Creating bin")

    result = make_bin(60.0, 40.0, 3.0)

    print("Showing result")

    show(style(result, color="blue", alpha=0.5), gradient=False)
