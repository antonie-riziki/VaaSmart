from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
from elevenlabs import stream, play
from io import BytesIO

import streamlit as st

import os

load_dotenv()

elevenlabs = ElevenLabs(
		api_key=os.getenv("ELEVENLABS_API_KEY"),
	)



def generate_speech(prompt):
	audio = elevenlabs.text_to_speech.convert(
			text=prompt,
			voice_id="JBFqnCBsd6RMkjVDRZzb",
		    model_id="eleven_multilingual_v2",
		    output_format="mp3_44100_128",

		)
	audio_bytes = b"".join(audio)
	audio_io = BytesIO(audio_bytes)

	st.audio(audio_io, format="audio/mp3")
