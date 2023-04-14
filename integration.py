from manim import *
vertices=[]
class GetAreaExample(Scene):
    def construct(self):
        plane = NumberPlane(x_length=10, y_length=6, x_range=[-5, 5], y_range=[-3, 3]).add_coordinates();
        circ = Circle(radius=1).move_to(plane.get_origin())
        sector = Sector(radius=1, angle=TAU/4, fill_opacity=0.5, color=RED).next_to(circ.get_center(),UP+RIGHT,buff=0)
        circle_label = MathTex(r"\text{Circle with radius 1}").next_to(circ, UP)
        
        self.play(FadeIn(plane))
        self.wait(2)
        self.play(Create(circ))
        self.play(Write(circle_label))
        self.wait(2)
        self.remove(circle_label)
        self.play(Create(sector))
        self.wait(2)
        ola=VGroup(plane,circ,sector)
        self.play(ola.animate.scale(0.5).move_to(LEFT*3))

        # self.play(plane.animate.scale(0.5).move_to(LEFT),circ.animate.scale(0.5).move_to(plane.get_origin()),sector.animate.scale(0.5).next_to(circ.get_center(),UP+RIGHT,buff=0))
        how_to_area=MathTex(r"\text{Area of Shaded Region =}\int_{0}^{1}\sqrt[2]{1-x^2}dx",width=70,font_size=90).next_to(plane,RIGHT)
        self.play(Write(how_to_area),run_time=4)
        self.wait(3)
        self.remove(how_to_area)



class pp(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoomed_camera_config={
                "default_frame_stroke_width": 2.5,  # Set the stroke width here
            },
            **kwargs
        )

    def construct(self):
        ax_1 = NumberPlane(x_length=10, y_length=6, x_range=[-5, 5], y_range=[-3, 3],
                           x_axis_config={
            "font_size":10
                           },
                           y_axis_config={
            "font_size":10
                           }).add_coordinates()
        
        def c(x):
            return np.sqrt(1-x**2)
        curve_1 = ax_1.plot(c,x_range=(0,1,0.001), color=PURE_RED)
        def create_rects(dx,where):
            return ax_1.get_riemann_rectangles(
                curve_1, x_range=[0, 1], dx=dx, color=YELLOW,stroke_width=0,input_sample_type=where,
            )
        rects=create_rects(0.1,"right")
        all=VGroup(ax_1,curve_1,rects)
        self.play(Create(ax_1, run_time=3))
        self.play(Create(curve_1),run_time=2)
        self.wait(2)
        self.play(Create(rects),run_time=3)
        self.remove(rects)
        self.remove(curve_1)
        self.remove(ax_1)
        self.add(all)
        self.play(ScaleInPlace(all, 3), run_time=2)
        self.wait(2)
        self.remove(rects)
        rects=create_rects(0.1,"left")
        rects.set_opacity(0.5)
        self.play(Create(rects),run_time=3)
        self.wait(3)
        self.remove(rects)
        rects=create_rects(0.01,"right")
        self.play(Create(rects),run_time=3)
        self.wait(2)
        self.activate_zooming(animate=True)
        self.play(self.zoomed_camera.frame.animate.scale(0.01),self.zoomed_camera.frame.animate.shift(ax_1.get_origin()+0.7 * UP+2.8*RIGHT))
        self.wait(4)
        self.get_zoomed_display_pop_out_animation()
        self.play(Uncreate(self.zoomed_display.display_frame), FadeOut(self.zoomed_camera.frame))
        self.get_zoomed_display_pop_out_animation()
        self.wait(3)
        self.remove(rects)
        rects=create_rects(0.0999,"right")
        self.play(Create(rects),run_time=3)
        self.wait(2)
        textx=Text("width", font_size=15)
        texty=Text("height", font_size=15)
        text_area=MathTex(r"\text{Area=Height}\times\text{Width}",font_size=40,fill_color=WHITE)
        text_tarea=MathTex(r"\text{Total Area=}\sum_{n=0}^{9} Height_{n}\times Width_{n}",font_size=40,fill_color=WHITE)
        for i,tab in enumerate(rects):
            val1=MathTex(r"P_{%d}" % i,font_size=20,fill_color=WHITE)
            val2 = MathTex(r"Q_{%d}" % i,font_size=20,fill_color=WHITE)
            self.play(Write(val1.next_to(tab.get_top(),UP*1)),run_time=0.1)
            self.play(Write(val2.next_to(tab.get_bottom(),DOWN*0.5)),run_time=0.1)
        
        
        self.add(rects[0])
        self.play(rects[0].animate.set_stroke(color=PURE_GREEN,width=4,opacity=2),run_time=2)
        self.play(Write(textx.next_to(rects[0].get_top(),UP*2)))
        self.play(Write(texty.next_to(rects[0].get_left(),LEFT)))
        self.play(Write(text_area.next_to(ORIGIN,RIGHT*2+DOWN*3)),run_time=3)
        self.play(Write(text_tarea.next_to(text_area.get_bottom(),DOWN*2)),run_time=5)
        for _ in rects:
            self.play(_.animate.set_stroke(width=4,color=PURE_GREEN,opacity=1),run_time=0.2)
        self.wait(5)

        



        
