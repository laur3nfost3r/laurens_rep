from manim import *
import streamlit as st
import numpy as np 

class CreateCircle1(ThreeDScene):
    def construct(self):

        # self.next_section("first section")
        # axes = ThreeDAxes()
        # circle = Circle()
        # slide = st.slider("pick a number!",1,10)
        # circle.set_fill(PINK, opacity=0.5)
        # line = Line()

        # self.add(line)
        # self.wait(1)
        # self.play(Rotate(Line(), angle=2*PI, about_point= LEFT, rate_func=linear))
        # self.add(circle)
        # self.wait(1)

        # self.next_section("second section")
        # self.add(axes)
        # self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES)
        # cylinder = Cylinder()
        # self.play(Transform(circle,cylinder))
        # self.wait(1)

        # self.next_section("third section")
        # cylinder.generate_target()
        # cylinder.target.shift(slide*UP)
        # self.add(cylinder)
        # self.play(MoveToTarget(cylinder))

        sections = 20
        for i in range(0,sections+1):
            theta = np.pi/2*i
            x = np.cos(theta)
            y=np.sin(theta)
            line = Line(start=(0,0,0), end=(x,y,0))
            self.wait(.1)
            self.add(line)


st.title('Bare bones')

c = CreateCircle1()
config.save_sections=True  
c.render()
# st.video("media/videos/1080p60/CreateCircle1.mp4")