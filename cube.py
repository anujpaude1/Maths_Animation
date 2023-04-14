from manim import *

class Try(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        axes.x_axis.color=RED
        axes.y_axis.color=GREEN
        axes.z_axis.color=BLUE
        cube = Cube(side_length=3, fill_opacity=0, stroke_width=2,stroke_color=WHITE)
        cube.move_to((1.5, 1.5, 1.5))
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)
        line = Line3D(start=np.array([0, 0, 0]), end=np.array([3, 3, 3]))
        cube.generate_points()
        self.play(FadeIn(axes),FadeIn(cube))
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.play(Create(line))
        self.wait(2)