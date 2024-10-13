# Voice-Controlled Circle Game

## Overview

This is a simple game where you can move a circle using your voice. The game utilizes the OpenAI API to convert voice commands into text, which are then transformed into instructions to control the circle's movement.

## How It Works

1. **Voice Input**: Press space and speak your commands into the microphone.
2. **Speech-to-Text**: The Whisper-1 API converts your voice into text.
3. **Prompt Engineering**: The text is processed with the GPT-4o-mini API to create movement instructions for the circle.
