import moviepy.editor
from tkinter.filedialog import *

vid="c:\\Users\\Admin\\Desktop\\upwork.mp4"
video=moviepy.editor.VideoFileClip(vid)

aud=video.audio
aud.write_audiofile("demo.mp3")
print("Your video converted")

