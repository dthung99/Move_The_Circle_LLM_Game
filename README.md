# Voice-Controlled Circle Game

## Overview

This is a simple game where you can move a circle using your voice. The game utilizes the OpenAI API to convert voice commands into text, which are then transformed into instructions to control the circle's movement.

## How It Works

1. **Voice Input**: Press space and speak your commands into the microphone.

2. **Speech-to-Text**: The Whisper-1 API converts your voice into text.

3. **Prompt Engineering**: The text is processed with the GPT-4o-mini API to create movement instructions for the circle.

## What you can do

1. **Movement**: Move the circle left, right, up, or down using your keyboard or voice commands.

2. **Change Color**: Change the circle's color by using voice commands.

## Demo

https://github.com/user-attachments/assets/15f0b0e5-373e-4362-a346-5394a3d2879a

## Getting Started

To download and run the application, follow these steps:

### Prerequisites

- Ensure you have Python 3.12.6 or later installed on your machine.
- You will need an OpenAI API key. Sign up at [OpenAI](https://openai.com) to obtain your key.

### Downloading the Application

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/dthung99/Move_The_Circle_LLM_Game.git
    ```

2. Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```

3. Set the OpenAI API Key

Before running the app, you need to set the OpenAI API key as an environment variable. Replace your-api-key with your actual API key:

On Linux/macOS:

    ```bash
    export OPENAI_API_KEY=your-api-key
    ```

On Windows (Command Prompt):

    export OPENAI_API_KEY=your-api-key

On Windows (PowerShell):

    ```bash
    $env:OPENAI_API_KEY="your-api-key"
    ```

4. Run the Application
    ```bash
    python main.py
    ```
