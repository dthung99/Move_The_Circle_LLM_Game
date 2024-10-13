from pydantic import BaseModel
from openai import OpenAI
from typing import Optional, Tuple

import pyaudio
import numpy as np
import wave

class UserInstruction(BaseModel):
    move_left: bool
    move_right: bool
    move_up: bool
    move_down: bool
    stop: bool
    change_color: bool
    red_in_rgb: Optional[int] = None
    green_in_rgb: Optional[int] = None
    blue_in_rgb: Optional[int] = None

class LLMHandler:
    def __init__(self) -> None:
        # Set up parameters for recording
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.RATE = 44100
        self.CHUNK = 1024
        # Create a PyAudio object
        self.audio = pyaudio.PyAudio()
        # No recording at the beginning
        self.recording = False
        # Start open AI model
        self.client = OpenAI()
        self.llm_instruction = None

    def start_recording(self):
        # Start recording
        stream = self.audio.open(format=self.FORMAT, channels=self.CHANNELS,
                                 rate=self.RATE, input=True,
                                 frames_per_buffer=self.CHUNK)
        print("Recording...")
        frames = []
        # Record for the specified duration
        self.recording = True
        while self.recording:
            data = stream.read(self.CHUNK)
            frames.append(data)

        print("Recording finished.")
        # Stop and close the stream
        stream.stop_stream()
        stream.close()
        # self.audio.terminate() # Do not need to terminate the audio

        # Save the recorded data as a WAV file
        with wave.open("output.wav", 'wb') as wf:
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.audio.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(frames))
            
        # Send the audio to open ai to get the script
        audio_file = open("output.wav", "rb")
        transcription = self.client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
            )
        
        # Prompt engineering to get the instruction from open AI                      
        control_intruction = self.client.beta.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You will receive user inputs to control a game character. You will return what the user wants to do. \
                    The options are to move left, right, up, down, stop, and change to a certain color."},
                {"role": "user", "content": transcription.text}
            ],
            response_format=UserInstruction,
        )
        
        self.llm_instruction = control_intruction.choices[0].message.parsed
            
    def stop_recording(self):
        self.recording = False             



