from manim import *
import streamlit as st

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen

class Shapes(Scene):
    def construct(self):
        triangle = Triangle()
        self.play(Create(triangle))



def main():

    scene = CreateCircle()
    scene.render()
    st.video("media/videos/1080p60/CreateCircle.mp4")

    next = Shapes()
    next.render()
    st.video("media/videos/1080p60/CreateCircle.mp4")

if __name__=="__main__":
    main()