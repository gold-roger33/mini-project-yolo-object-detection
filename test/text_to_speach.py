from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO

# Text to be converted to speech
text = "Hello, how are you? I am Mahesh Mahesh. This is my day, boy."

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine
tts = gTTS(text=text, lang=language, slow=False)

# Converting gTTS object to an AudioSegment object
audio_data = tts.get_audio_data()
audio = AudioSegment.from_file(BytesIO(audio_data), format="mp3")

# Play the audio
play(audio)
