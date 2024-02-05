from manim import *
import streamlit as st

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        line = Line()
        
        self.play(Create(line))  # show the circle on screen
        self.wait(1)
        self.play(ReplacementTransform(line, circle))




def main():

    scene = CreateCircle()
    scene.render()
    st.video("media/videos/1080p60/CreateCircle.mp4")


if __name__=="__main__":
    main()