# Manim Intro Video Project

## Overview
This project contains an introductory animation created using **Manim Community v0.19.0**. The animation serves as a personal introduction for an internship at **Imran's Lab**, including opening and closing branding with the company logo and colors.

## Features
- Opening Branding: 10-second intro with Imran's Lab branding.
- Main Content: Personal introduction including name, fun fact, and excitement for the internship.
- Closing Branding: 10-second outro with consistent branding for future videos.
- Clean and modular Manim code for easy reuse.

## Tools & Libraries
- **Python 3.10**
- **Manim Community v0.19.0**
- **Pydub** (for audio, optional)
- **VS Code** (for editing and running scripts)

## File Structure
C:/manim/
│
├─ intro.py # Main Manim script
├─ test_scene.py # Example scene for testing
├─ media/ # Generated videos and partial files
└─ .venv/ # Virtual environment


## How to Run
#C:/manim/
│
├─ intro.py # Main Manim script
├─ test_scene.py # Example scene for testing
├─ media/ # Generated videos and partial files
└─ .venv/ # Virtual environment


## How to Run
## 1. Activate virtual environment:
```powershell
.venv\Scripts\Activate.ps1


## Run the Manim scene:

python -m manim -pql intro.py IntroVideo


Check the output video in media/videos/intro/480p15/IntroVideo.mp4.

Notes

Make sure ffmpeg is installed and added to your PATH to avoid Pydub warnings.

The branding colors and slogans were inspired by Imran's Lab
 websites.

Follow modular coding practices to allow reuse in future projects.

## License

This project is created for educational purposes at Imran's Lab Internship and is not intended for commercial use.
