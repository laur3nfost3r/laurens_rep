from manim import *
import streamlit as st

class CreateCircle(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle = Circle()
        slide = st.slider("pick a number!",1,10)
        circle.set_fill(PINK, opacity=0.5)
        line = Line()
        self.add(line)
        self.wait(1)
        self.play(Rotate(Line(), angle=2*PI, about_point= LEFT, rate_func=linear))
        self.add(circle)
        self.wait(1)
        self.add(axes)
        self.move_camera(phi=70 * DEGREES, theta=30 * DEGREES)
        cylinder = Cylinder()
        self.play(Transform(circle,cylinder))
        self.wait(1)
        cylinder.generate_target()
        cylinder.target.shift(slide*UP)

        self.add(cylinder)
        self.play(MoveToTarget(cylinder))
        #slider crashes for 1? 

st.title('Bare bones')

c = CreateCircle()
c.render()
st.video("media/videos/1080p60/CreateCircle.mp4")