from manim import *

class Try(Scene):
    graph = Axes(
            x_range=[-6, 8, 1],
            y_range=[-4, 5, 1],
            tips=True,
            x_length=10,
            y_length=6.42,
            axis_config={
            "include_numbers": True,
            "tick_size":0.08,
            "tip_length":0.05,
            "font_size":20,
            "tip_width":0.2,
            "tip_height":0.2
            }
        )
        # Name of axis
    name = graph.get_axis_labels(Text("X").scale(0.5),Text("Y").scale(0.5))
    p1 = Dot(graph.coords_to_point(-3, 1/8), color=RED_D, radius=0.05)
    p2 = Dot(graph.coords_to_point(-3, 1/8), color=RED_D, radius=0.05)