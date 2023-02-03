from gtts import gTTS
import os

text = "The Raven By Edgar Allan Poe. Once upon a midnight dreary, while I pondered, weak and weary,\nOver many a quaint and curious volume of forgotten lore,\nWhile I nodded, nearly napping, suddenly there came a tapping,\nAs of someone gently rapping, rapping at my chamber door.\n'Tis some visitor, I muttered, tapping at my chamber door;\nOnly this and nothing more."

tts = gTTS(text=text, lang='en')
tts.save("poem.mp3")

# os.system function is used to play the MP3 file using the mpg321 command-line tool.
# os.system("mpg321 hello.mp3")
