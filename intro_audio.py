from gtts import gTTS

# Text to be spoken in the video
full_text = (
    "Welcome to Imran's Lab! "
    "Hi! I'm Bushra Jahan. "
    "Fun fact: I love coding and exploring new tech. "
    "Excited to join this internship! "
    "Thank you for watching. Imran's Lab - Learn. Innovate. Repeat."
)

# Create TTS audio in female voice
tts = gTTS(text=full_text, lang='en', tld='com.au')  # Australian female accent
tts.save("intro_audio.mp3")
from gtts import gTTS

# Your narration text
text = """
Welcome to Imran's Lab! Innovate. Learn. Create.
Hi! I'm Bushra Jahan. Fun fact: I love coding and exploring new tech!
Excited to join this internship! Thank you for watching.
"""

# Convert text to speech
tts = gTTS(text=text, lang='en')

# Save as mp3
tts.save("intro_audio.mp3")
print("Audio file created successfully!")

