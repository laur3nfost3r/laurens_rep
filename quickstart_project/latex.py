import streamlit as st
from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello world", font_size=144)
        self.add(text)

c = HelloWorld()
c.render()
st.video("media/videos/1080p60/HelloWorld.mp4")