
import cadquery as cq

from cadquery.vis import show, style

def make_bin(width: float, height:float) -> cq.Workplane:

    # outside_fillet = width/10.0
    # inside_fillet = width/12.0
    #
    # inside_width = width * 0.9
    # inside_depth = height * 0.9
    #
    # shell = cq.Workplane("XY").box(width, width, height).edges("|Z").fillet(outside_fillet)
    #
    # cut = shell.faces(">Z").workplane().rect(inside_width, inside_width).cutBlind(until=-inside_depth)
    #
    # final = cut.edges("|Z").fillet(inside_width)

    box_dim = 60
    box_wall = 6

    outside_fillet = box_wall / 2
    inside_fillet = box_wall / 2

    model = cq.Workplane("XY") \
        .box(box_dim, box_dim, box_dim) \
        .edges('|Z').fillet(5) \
        .faces(">Z").workplane() \
        .rect(box_dim - box_wall, box_dim - box_wall) \
        .cutBlind(until=-(box_dim - (box_wall / 2))) \
        .edges("|Z").fillet(2) \
        .faces("<Z[1]").edges().fillet(2)

    return model

if __name__ == "__main__":

    print("Creating bin")

    result = make_bin(40.0, 20.0)

    print("Showing result")
    # show(result, alpha=0.5, gradient=False)
    show(style(result, color="blue", alpha=0.5), gradient=False)