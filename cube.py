from manim import *


class Try(ThreeDScene):
    def construct(self):
        ax=ThreeDAxes()
        ax.x_axis.color=RED
        ax.y_axis.color=GREEN
        ax.z_axis.color=BLUE
        cube = Cube(side_length=2, fill_opacity=0, stroke_width=2,stroke_color=WHITE)
        self.add(ax)
        cube.move_to((1, 1, 1))
        self.set_camera_orientation(phi=75*DEGREES,theta=-45*DEGREES)
        cube_diagonal_1 = Line3D(start=np.array([0, 0, 0]), end=np.array([2, 2, 2]),color=ORANGE)
        cube_diagonal_2 = Line3D(start=np.array([0, 0, 2]), end=np.array([2, 2, 0]),color=ORANGE)
        cube_diagonal_1_label=MathTex(r"a\sqrt{3}",font_size=25).next_to(cube_diagonal_1.get_center())
        square_diagonal_1=Line3D(start=np.array([0, 0, 0]), end=np.array([2, 2, 0]))
        square_diagonal_1_label=MathTex(r"a\sqrt{2}",font_size=25).next_to(square_diagonal_1.get_center())
        corners = np.array([[1,1,1],[0,0,0],[2,0,0],[2,2,0],[0,2,0],[0,0,2],[2,0,2],[2,2,2],[0,2,2]])*3-np.array([2,2,2])
        
        line_from_center=Line3D(start=np.array([1, 1, 1]), end=np.array([1, 1, 0]))
        line_from_center_height=MathTex(r"\frac{a}{2}",font_size=17).next_to(line_from_center.get_center())
        line_from_center_base=MathTex(r"\frac{a\sqrt{2}}{2}",font_size=17).next_to((square_diagonal_1.get_center()+square_diagonal_1.get_start())/2+IN*0.2)
        line_from_center_hypo=MathTex(r"\frac{a\sqrt{3}}{2}",font_size=17).next_to((cube_diagonal_1.get_center()+cube_diagonal_1.get_start())/2+OUT*0.5+DOWN*0.3)
        
        #  angle calculation
        angle1=ArcBetweenPoints([0.8,0.8,0.8],[1,1,0.8],color=YELLOW_C)
        angle2=ArcBetweenPoints([0.7,0.7,0.7],[1.3,1.3,0.7],color=YELLOW_C)
        angle3=ArcBetweenPoints([1.2,1.2,0.8],[1.2,1.2,1.2],color=PINK)
        angle1_label = MathTex(r"54.735^\circ",font_size=20).next_to(angle1.get_center())
        angle2_label=MathTex(r"109.47^\circ",font_size=20).next_to(angle2.get_center())
        angle3_label=MathTex(r"70.53^\circ",font_size=20).next_to(angle3.get_center())
        angle_1 = MathTex(r"\theta=\sin^{-1}\left(\frac{p}{h}\right)")
        angle_2 = MathTex(r"\theta=\sin^{-1}\left(\frac{\frac{a\sqrt{2}}{2}}{\frac{a\sqrt{3}}{2}}\right)")
        angle_3 = MathTex(r"\theta=\sin^{-1}\left(\frac{\sqrt{2}}{\sqrt{3}}\right)")
        angle_4 = MathTex(r"\theta=54.735^\circ").next_to(angle1.get_center())
        
        gp_a=VGroup( angle_1, angle_2, angle_3,angle_4).arrange(DOWN, aligned_edge=LEFT).move_to(UP*2+RIGHT*4.5)


        label1=Text("a",font_size=25).next_to(cube.get_bottom()+0.2*DOWN+1.2*IN+0.5*LEFT)
        label2=Text("a",font_size=25).next_to(cube.get_right()+1.2*DOWN+0.2*LEFT)
        label3=Text("a",font_size=25).next_to(cube.get_right()+0.2*DOWN+1.2*IN+0.5*LEFT)
        label4=Text("a",font_size=25).next_to(cube.get_left()+1.2*DOWN+0.2*RIGHT)

        #calculation text
        s_diagonal_1=MathTex(r"\sqrt{a^2+a^2}")
        s_diagonal_2=MathTex(r"\sqrt{2a^2}")
        s_diagonal_3=MathTex(r"a\sqrt{2}")
        gp_s_diagonal=VGroup(s_diagonal_1,s_diagonal_2,s_diagonal_3).arrange(DOWN, aligned_edge=LEFT).move_to(UP*2+RIGHT*4.5)
        
        
        c_diagonal_1=MathTex(r"\sqrt{(a\sqrt{2})^2+a^2}")
        c_diagonal_2=MathTex(r"\sqrt{{2a^2+a^2}")
        c_diagonal_3=MathTex(r"\sqrt{{3a^2}")
        c_diagonal_4=MathTex(r"a\sqrt{{3}")
        gp_c_diagonal=VGroup(c_diagonal_1,c_diagonal_2,c_diagonal_3,c_diagonal_4).arrange(DOWN, aligned_edge=LEFT).move_to(UP*2+RIGHT*4.5)

        
        #only image
        # self.add(ax,cube,cube_diagonal_1,square_diagonal_1,line_from_center,line_from_center,cube_diagonal_2,angle1,angle2,angle3)
        # self.add_fixed_in_frame_mobjects(gp_s_diagonal.move_to(UP*2+RIGHT*4.5),gp_c_diagonal.move_to(UP*2+LEFT*4.5))
        # self.add_fixed_orientation_mobjects(line_from_center_base,line_from_center_height,line_from_center_hypo)
        
        #without animation
        # self.begin_ambient_camera_rotation(rate=0.1)
        # self.add(ax,cube,cube_diagonal_1,square_diagonal_1)
        # self.add_fixed_orientation_mobjects(label1,label2,label3,label4,cube_diagonal_1_label,square_diagonal_1_label)
        # self.wait(7)
        # self.stop_ambient_camera_rotation()
        
        

        #with animation

    
        self.add(ax,cube)
        self.play(FadeIn(cube))
        self.wait(2)
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(1)
        self.add_fixed_orientation_mobjects(label1,label2,label3)
        self.wait(5)
        self.play(Create(cube_diagonal_1),run_time=2)
        self.wait(1)
        self.play(Create(cube_diagonal_2),run_time=2)
        self.play(Create(angle2),Create(angle3),run_time=3)
        self.wait(3)
        self.remove(cube_diagonal_2,angle2,angle3)
        self.remove_fixed_orientation_mobjects(label3)
        self.play(Create(square_diagonal_1),run_time=3) 
        self.add_fixed_in_frame_mobjects(gp_s_diagonal)
        self.wait(3)
        self.add_fixed_orientation_mobjects(square_diagonal_1_label)
        self.remove_fixed_in_frame_mobjects(gp_s_diagonal)
        self.remove(gp_s_diagonal)
        self.add_fixed_orientation_mobjects(label4)
        self.wait(3)
        self.add_fixed_in_frame_mobjects(gp_c_diagonal)
        self.wait(5)
        self.add_fixed_orientation_mobjects(cube_diagonal_1_label)
        self.remove_fixed_in_frame_mobjects(gp_c_diagonal)
        self.remove(gp_c_diagonal)
        self.wait(1)
        self.play(Create(line_from_center))
        self.play(Create(angle1),run_time=3)
        self.add_fixed_orientation_mobjects(line_from_center_base,line_from_center_hypo)
        self.wait(3)
        self.add_fixed_in_frame_mobjects(gp_a)
        self.wait(5)
        self.add_fixed_orientation_mobjects(angle1_label)
        self.wait(3)
        self.play(Create(angle2))
        self.remove(angle1)
        self.remove_fixed_orientation_mobjects(angle1_label)
        self.add_fixed_orientation_mobjects(angle2_label)
        self.wait(3)
        self.play(Create(angle3),run_time=3)
        self.wait(1)
        self.add_fixed_orientation_mobjects(angle3_label)
        self.stop_ambient_camera_rotation()
        
        