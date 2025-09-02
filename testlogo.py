from manim import *

class TestLogo(Scene):
    def construct(self):
        logo = ImageMobject("logo.jpg")  # Use exact file name
        logo.scale(0.5)                  # Resize if too big
        logo.to_edge(UP)                 # Move it to top

        self.play(FadeIn(logo))          # Show logo
        self.wait(2)
        self.play(FadeOut(logo))         # Hide logo
