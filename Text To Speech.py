from gtts import gTTS
import os

# Open function to open & read the file
source = "தமிழ் வாழ்க"

# Language in which you want to convert
language = "ta"

# Passing the text and language to the engine, here we have marked slow=False. Which tells the module that the converted audio should have a high speed
file = gTTS(text=source, lang=language, slow=False)

# Saving the converted audio in a mp3 file
file.save("output.mp3")

# Playing the converted file
os.system("output.mp3")
