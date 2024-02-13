from manim import *
import streamlit as st

class Shapes(Scene):
    def construct(self):
        line = Line()
        line.set_fill(BLUE, opacity=0.5)

        circle = Circle()
        circle.set_fill(GREEN, opacity = 0.5)
        

        line.shift(LEFT)
        self.play(Create(line))
        
class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation

c = Shapes()
d = SquareToCircle()
d.render()
c.render()
st.video("media/videos/1080p60/Shapes.mp4")

