import streamlit as st
from manim import *
import numpy as np 

class Loops(ThreeDScene):
    def construct(self):
        sections = 20
        for i in range(0,sections+1):
            theta = np.pi/2*i
            x = np.cos(theta)
            y=np.sin(theta)
            line = Line(start=(0,0,0), end=(x,y,0))
            self.add(line)

c = Loops()
c.render()
st.video("media/videos/1080p60/Loops.mp4")
