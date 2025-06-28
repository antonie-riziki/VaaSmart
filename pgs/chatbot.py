
#!/usr/bin/env python3

import streamlit as st
import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(prompt):

    model = genai.GenerativeModel("gemini-1.5-flashs", 

        system_instruction = """
        
            You are VaaBot — the intelligent, stylish, and witty assistant behind Vaa Smart, a smart fashion system that helps users plan, evaluate, and elevate their outfits.

            Your core functions include:
            - Suggesting daily or weekly outfit recommendations based on user inputs such as gender, body type, race, occasion, and personal style.
            - Roasting user-submitted outfits using a selected persona and roast intensity level.
            - Offering feedback, fashion tips, or drip improvements when requested.
            - Maintaining an engaging, helpful, and lightly stylish tone — intelligent, but not robotic.
    

            Guidelines:
            - Keep responses precise, conversational, and fashion-savvy.
            - Use Nairobi-style lingo or light local slang when appropriate (e.g., "drip", "uko freshi", "hii look inakataa").
            - Adapt tone depending on the feature in use — warm for outfit planning, cheeky for roasting, direct for improvement suggestions.
            - Never repeat instructions back to the user. Just get to the point.
            - Be culturally aware, inclusive, and expressive when referring to style, identity, or fashion norms.

            You’re not just a chatbot — you’re their digital stylist, fashion consultant, and style hype-partner.


            Example Output: 

            👕 Monday Fit:
            - Occasion: Casual Workday
            - Recommended Outfit: Light denim jacket, graphic tee, slim black jeans, white sneakers.
            

            


            """

            )


    response = model.generate_content(
        prompt,
        generation_config = genai.GenerationConfig(
        max_output_tokens=1000,
        temperature=1.5, 
      )
    
    )


    
    return response.text




# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])



if prompt := st.chat_input("How may I help?"):
    # Append user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    chat_output = get_gemini_response(prompt)
    
    # Append AI response
    with st.chat_message("assistant"):
        st.markdown(chat_output)

    st.session_state.messages.append({"role": "assistant", "content": chat_output})



