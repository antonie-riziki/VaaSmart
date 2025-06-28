from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64
import os
import streamlit as st


from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

contents = ('Hi, can you create a 3d rendered image of a female person '
            'with a modern african inspired outfit featuring slim-fit white linen shirt, sleeves rolled up '
            'tailored navy blue african print pants with a modern tapered cut, light grey linen blazer'
            'brown leather loafers, slim patterned silk pocket square classic brown leather belt')

def google_image_generator(prompt):
  response = client.models.generate_content(
      model="gemini-2.0-flash-preview-image-generation",
      contents=prompt,
      config=types.GenerateContentConfig(
        response_modalities=['TEXT', 'IMAGE']
      )
  )

  for part in response.candidates[0].content.parts:
    if part.text is not None:
      print(part.text)
    
    elif part.inline_data is not None:
      image = Image.open(BytesIO((part.inline_data.data)))
      # image.save('gemini-native-image.png')
      # image.show()
      st.image(image, use_container_width=True)


