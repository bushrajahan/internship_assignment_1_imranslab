from manim import *

class IntroVideo(Scene):
    def construct(self):
        # ---------- Add narration audio ----------
      
        # ---------- Opening Branding (10 seconds) ----------
       # Wait enough for audio to play
        self.add_sound("intro_audio.mp3")     
       
        logo = ImageMobject("logo.jpg")  # Use exact file name
        logo.scale(0.5)                  # Resize if too big
        logo.to_edge(UP)                 # Move it to top

          # Make sure this file is in the same folder
      
        self.play(FadeIn(logo))          # Show logo
      
        self.play(FadeOut(logo))   
        
      
        # ---------- Main Content (Your Introduction) ----------
     

        opening_text = Text("Welcome to Imran's Lab!", font_size=48, color=BLUE)
        slogan = Text("Innovate. Learn. Create.", font_size=36, color=YELLOW).next_to(opening_text, DOWN)
        self.play(Write(opening_text))
        self.play(FadeIn(slogan))
        self.wait(3)
        self.play(FadeOut(opening_text), FadeOut(slogan))
        
    
        
        intro_title = Text("Hi! I'm Bushra Jahan", font_size=48, color=GREEN)
        fun_fact = Text("Fun Fact: I love coding & exploring new tech!", font_size=36).next_to(intro_title, DOWN)
        excitement = Text("Excited to join this internship!", font_size=36).next_to(fun_fact, DOWN)
        
        self.play(Write(intro_title))
        self.play(FadeIn(fun_fact))
        self.play(FadeIn(excitement))
        self.wait(4)
        self.play(FadeOut(intro_title), FadeOut(fun_fact), FadeOut(excitement))
        
        # ---------- Closing Branding (10 seconds) ----------
        logo = ImageMobject("logo.jpg")  # Use exact file name
        logo.scale(0.5)                  # Resize if too big
        logo.to_edge(UP)                 # Move it to top

        self.play(FadeIn(logo))          # Show logo
        self.wait(2)
        self.play(FadeOut(logo))    
        closing_text = Text("Thank you for watching!", font_size=48, color=BLUE)
        closing_slogan = Text("Imran's Lab - Learn. Innovate. Repeat.", font_size=36).next_to(closing_text, DOWN)
        self.play(Write(closing_text))
        self.play(FadeIn(closing_slogan))
        self.wait(3)
        self.play(FadeOut(closing_text), FadeOut(closing_slogan))
