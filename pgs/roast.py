
# from __future__ import annotations

import streamlit_scrollable_textbox as stx
import streamlit as st 
import sys

from PIL import Image


sys.path.insert(1, './modules')
print(sys.path.insert(1, '../modules/'))


from func import get_fashion_roast
from voice_generation import generate_speech

from dotenv import load_dotenv

load_dotenv()



st.markdown(
    """
    <div class=title>
        <div style=" justify-content: center;">
            <h1 style="text-align: center; padding: 5px; color: #F52887;">Vaa Smart 👗</h1>
            <p style="text-align: center;">Reimagining Fashion with Tech – One Closet at a Time</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.image('https://i.ytimg.com/vi/SQA1zhxRK2c/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBlG-OXEcAIx1EQhTiKqQLdDkAEsw', width=900)



roast_personas = {
    

    "👴 Kabogo the ICT CS": """You're Kenya's Cabinet Secretary for ICT and Digital Affairs, with a sharp tongue and 
    zero tolerance for digital disorder — especially when it comes to dressing. You speak like you're addressing 
    a press briefing or parliamentary session. Use government terms like 'non-compliance,' 'public concern,' and 
    'policy breach' to critique the outfit. Throw in a reference to digitization, national image, or budget misuse. 
    Maintain a serious tone while delivering humorous and sarcastic commentary. You are disappointed, not amused.""",

    "👵 Grandma Rosie": """You're a fashion-forward grandmother who's seen it all and can't believe 
    what the kids are wearing these days. Mix genuine concern with witty observations. Compare this to 
    what people wore 'in your day' and throw in at least one 'Back in my time...' reference. Be loving 
    but thoroughly unimpressed.""",

    "💅 Kathy the Instagram Influencer": """You're a self-proclaimed fashion influencer with 127 followers 
    who thinks they're the next big thing. Use at least 2 made-up hashtags, reference a random fashion 
    week, and explain why this outfit isn't 'giving what it's supposed to give.' Be dramatic about the 
    aesthetic and vibes.""",

    "🧙‍♂️ Fashion Wizard Babu Wekesa": """You're a 700-year-old fashion wizard who has seen the rise and fall 
    of trends across galaxies. You use mystical and ancient fashion wisdom to judge the outfit. Mention 
    long-lost 'Drip Scrolls' or fashion spells gone wrong. Speak in cryptic, wise tones while roasting hard.""",

    "🧑‍⚖️ Judge Judith Style Court": """You're a no-nonsense courtroom judge presiding over the fashion court. 
    Treat the outfit like a criminal case. Use phrases like 'You stand accused of...', and issue a final 
    verdict. Be firm, sarcastic, and legally savage.""",

    "🎤 MC Teezy – Drip Battle Rapper": """You're an underground rap MC who roasts outfits in freestyle. Use 
    rhyme and rhythm to destroy the fit. Think ‘8 Mile’ meets fashion critique. End with a punchline that 
    slams the look creatively. Be loud, lyrical, and ruthless.""",

    "🎓 Professor Dripstein": """You're a tenured fashion professor at the University of Style. Use intellectual 
    jargon and over-the-top academic analysis to critique the outfit. Mention fake studies, imaginary 
    metrics, and deliver conclusions with deadpan sarcasm.""",

    "☕ Auntie Njeri from the Balcony": """You're a sharp-tongued Kenyan auntie who sees everything from her 
    balcony while sipping tea. Mix Swahili with sarcasm. Be brutally honest, throw family shade, and act 
    like this outfit brings shame to the entire estate.""",

    "👽 Zlork from Planet Glorb": """You're an alien fashion analyst from the planet Glorb. Earth outfits confuse 
    you. Compare the clothes to strange alien customs or materials. Misinterpret obvious fashion choices 
    hilariously and mention how 'this would never pass on Glorb.'""",

    "🎭 Sir Drip-a-Lot (Shakespearean Critic)": """You're a flamboyant Shakespearean-style fashion critic. Use 
    old English, dramatic metaphors, and theatrical flair. Reference 'ye olde outfit tragedies' and 
    deliver your roast like it's a royal proclamation.""",

    "😇 Therapist Toni": """You're a calm, kind therapist who gently roasts while pretending to help. Ask deep 
    questions like 'What were you feeling when you chose this jacket?' Make it feel like a counseling 
    session while lightly destroying their outfit choices with empathy and passive aggression."""
}




with st.sidebar:

    uploaded_file = st.file_uploader('Upload Your Drip', type=['jpg', 'jpeg', 'png', 'webp', 'bitmap', 'gif'])

    

    if uploaded_file is not None:

        drip_image = Image.open(uploaded_file)

        selected_style = st.selectbox(
            "Choose your fashion critic:",
            options=list(roast_personas.keys()),
            index=0
        )

        # intense_level = st.slider(['Light','Medium', 'Dark'])

        intensity = st.select_slider(
            "Choose your roast intensity:",
            options=[
                "☕ Light Roast",   
                "🔥 Medium Roast", 
                "💀 Dark Roast"   
            ],
            value="🔥 Medium Roast"  
        )

        add_info = st.text_area('additional info (optional)', value=None, height=115)




col1, col2= st.columns(2)

with col1:
    roast_button = st.button('Roast My Fit', use_container_width=True, type='primary')


with col2:
    level_drip_button = st.button('Leve Up the Look', use_container_width=True, type='primary')




col11, col12 = st.columns(2)


if roast_button and uploaded_file and selected_style and intensity and add_info is not None:
    base_prompt = roast_personas[selected_style] + add_info
    roast_text = get_fashion_roast(drip_image, selected_style, intensity, base_prompt)

    with col11:
        st.image(uploaded_file)
        # generate_speech(roast_text) # Remember to uncomment this line for presentation

    with col12:
        

        st.markdown("""
                <style>
                .scroll-box {
                    max-height: 450px;
                    overflow-y: scroll;
                    padding: 10px;
                    border: 1px solid #ccc;
                    border-radius: 8px;
                    
                }
                </style>
            """, unsafe_allow_html=True)

        # Then display the formatted Markdown content in a scrollable box
        # st.markdown(f'<div class="scroll-box">{get_fashion_roast(drip_image, selected_style, intensity, base_prompt)}</div>', unsafe_allow_html=True)

        st.markdown(f'<div class="scroll-box">{roast_text}</div>', unsafe_allow_html=True)
        

else:
    st.warning("Please upload an image and select a roast style and intensity before roasting your fit.")


if level_drip_button:

    with col11:
        st.image(uploaded_file)

    with col12:
        col12_1, col12_2 = st.columns(2)

        with col12_1:
            weather = st.selectbox('Season', ['Any', 'Winter', 'Summer', 'Autumn', 'Spring', 'Monsoon'])
            occassion = st.selectbox("What's the occasion?", ["Casual", "Formal", "Wedding", "Work/Office", "Outdoor Event", "Party", "Religious Event", "Other"])
            
            if occassion == "Other":
                occassion = st.text_input('please specify...')

        with col12_2:
            mood = st.selectbox('Mood', ['Elegant', 'Energetic', 'Happy','Lazy','Motivated','Romatic', 'Confident','Chill', 'Adventurous', 'Classy','Bold'])
            personal_style = st.multiselect("Describe your personal style", ["Chic", "Urban", "Bold Prints", "Minimalist", "Boho", "Vintage", "Modern African", "Streetwear"])


        st.button('🪄 Style Upgrade', use_container_width=True, type='primary')




