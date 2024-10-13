import wave
import pyaudio

# Define audio parameters
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

with wave.open('output.wav', 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(2)  # 2 bytes for paInt16
    wf.setframerate(RATE)
    print(type(wf))
    
audio_file= open("output.wav", "rb")
print(type(audio_file))
