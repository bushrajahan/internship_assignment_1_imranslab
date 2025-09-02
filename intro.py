from manim import *

# Change the class name to match your scene when running
class IntroVideo(Scene):
    def construct(self):
        # ---------- Opening Branding (10 seconds) ----------
        opening_text = Text("Welcome to Imran's Lab!", font_size=48, color=BLUE)
        slogan = Text("Innovate. Learn. Create.", font_size=36, color=YELLOW).next_to(opening_text, DOWN)
        self.play(Write(opening_text))
        self.play(FadeIn(slogan))
        self.wait(3)  # Wait 3 seconds, you can adjust timing
        self.play(FadeOut(opening_text), FadeOut(slogan))
        
        # ---------- Main Content (Your Introduction) ----------
        intro_title = Text("Hi! I'm Bushra Jahan", font_size=48, color=GREEN)
        fun_fact = Text("Fun Fact: I love coding & exploring new tech!", font_size=36).next_to(intro_title, DOWN)
        excitement = Text("Excited to join this internship!", font_size=36).next_to(fun_fact, DOWN)
        
        self.play(Write(intro_title))
        self.play(FadeIn(fun_fact))
        self.play(FadeIn(excitement))
        self.wait(4)  # Adjust time for how long you want it displayed
        self.play(FadeOut(intro_title), FadeOut(fun_fact), FadeOut(excitement))
        
        # ---------- Closing Branding (10 seconds) ----------
        closing_text = Text("Thank you for watching!", font_size=48, color=BLUE)
        closing_slogan = Text("Imran's Lab - Learn. Innovate. Repeat.", font_size=36, color=YELLOW).next_to(closing_text, DOWN)
        self.play(Write(closing_text))
        self.play(FadeIn(closing_slogan))
        self.wait(3)
        self.play(FadeOut(closing_text), FadeOut(closing_slogan))
