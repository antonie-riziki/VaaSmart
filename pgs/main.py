
from __future__ import annotations

import streamlit as st 
import sys
import folium


from streamlit_folium import st_folium


sys.path.insert(1, './models')
print(sys.path.insert(1, '../models/'))


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

st.image('https://www.eu-startups.com/wp-content/uploads/2023/11/Fahion-tech-min.png', width=900)


body = st.container()
with body:

	# ================== About Us ================== ================== #

    st.write("<h3 style='text-align: left; color: #3EA99F; margin-bottom: 1px;'>About Us</h3>", unsafe_allow_html=True)
    st.write("<h6 style='text-align: left; color: #3EA99F; margin-bottom: 1px;'>We champion individuality and self-expression through personalized fashion</h6>", unsafe_allow_html=True)

    st.write('''

        At Vaa Smart, we blend AI with fashion to revolutionize how you dress, shop, and express yourself. 
        Whether you're looking for daily outfit inspiration, a personalized fashion roast, or nearby stores that 
        sell your favorite looks — Vaa Smart is your virtual stylist, critic, and shopping assistant in one. Designed with 
        creativity and convenience at its core, we make intelligent fashion fun, accessible, and smartly local

        \nOur mission is to empower individuals to express their identity through intelligent fashion. We aim to seamlessly 
        blend artificial intelligence, creativity, and local discovery to transform how people dress, shop, and engage with 
        style — making personalized fashion guidance accessible, fun, and deeply human. We believe that style is not just about 
        what you wear, but how confidently you live.
        ''')





# ================== Our Services ================== ================== #

    st.write("<h3 style='text-align: left; color: #3EA99F; margin-bottom: 1px;'>What We Do</h3>", unsafe_allow_html=True)

    disaster_mgt, health, youth_dvp = st.columns(3, vertical_alignment="center")
    special_pgm, natl_society, crisis_resp = st.columns(3, vertical_alignment="center")

    with disaster_mgt:
        cont1 = st.container(border=True)
        cont1.write("<h5 style='text-align: center; margin-bottom: 1px;'>🎯 AI-Generated Outfits</h5>", unsafe_allow_html=True)
        cont1.write('''We use advanced generative models to create complete daily outfit suggestions based on your preferences, location, 
                    and style trends — tailored just for you. ''')


    with health:
        cont2 = st.container(border=True)
        cont2.write("<h5 style='text-align: center; margin-bottom: 1px;'>🎨 Visual Outfit Rendering</h5>", unsafe_allow_html=True)
        cont2.write('''See your look before you wear it! Our image generation engine turns text-based outfits into vivid visuals so you 
                    can preview your style in real-time.''') 


    with youth_dvp:
        cont3 = st.container(border=True)
        cont3.write("<h5 style='text-align: center; margin-bottom: 1px;'>🤖 Fashion Roasts \n(Just for Fun)</h5>", unsafe_allow_html=True)
        cont3.write('''Need a little tough love? Our voice-enabled AI roast gives you a playful nudge when your fashion choices go off track. 
                    It’s witty, honest, and never boring.''') 


    with special_pgm:
        cont4 = st.container(border=True)
        cont4.write("<h5 style='text-align: center; margin-bottom: 1px;'>🛍️ Nearby Store \nDiscovery</h5>", unsafe_allow_html=True)
        cont4.write('''We help you find local shops that sell items from your generated outfit — using smart location tools and open data mapping 
                    for cost-free, privacy-friendly results.''') 


    with natl_society:
        cont5 = st.container(border=True)
        cont5.write("<h5 style='text-align: center; margin-bottom: 1px;'>🗺️ Smart Map \nIntegration</h5>", unsafe_allow_html=True)
        cont5.write('''Our interactive map shows you nearby stores that match your fashion needs — along with ratings, directions, 
                    and store details, right inside the app.''') 


    with crisis_resp: 
        cont5 = st.container(border=True)
        cont5.write("<h5 style='text-align: center; margin-bottom: 1px;'>🎙️ Voice-to-Style \nExperience</h5>", unsafe_allow_html=True)
        cont5.write('''From speaking your preferences to listening to outfit breakdowns, we’re bringing fashion to life through audio, making 
                    your journey stylish and engaging — hands-free.''') 


    # ================== Our Partners ================== ================== #

    st.write("<h3 style='text-align: left; color: #3EA99F; margin-bottom: 1px;'>Our Partners</h3>", unsafe_allow_html=True)
    # st.write("<h6 style='text-align: left; margin-bottom: 1px;'>here are some of our partners</h6>", unsafe_allow_html=True)

    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    with col1:
        st.image('https://wp-sms-pro.com/wp-content/uploads/2019/04/africas-talking.png', width=150)

    with col2:
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/8/8a/Google_Gemini_logo.svg/2560px-Google_Gemini_logo.svg.png', width=150)

    with col3:
        st.image('https://biz.prlog.org/Vue_ai/logo.png', width=150)

    with col4:
        st.image('https://1000logos.net/wp-content/uploads/2022/02/Jumia-Logo.png', width=150)

    with col5:
        st.image('https://cdn.freelogovectors.net/wp-content/uploads/2020/09/mr-price-logo.png', width=150)

    with col6:
        st.image('https://www.fashioncity-outlet.gr/wp-content/uploads/2020/01/img_LCWaikiki.png', width=150)

    with col7:
        st.image('https://www.verve.vc/wp-content/uploads/2021/01/Fashwell_colour.png', width=150)



    # ================== Contact US ================== ================== #	

    st.write("<h3 style='text-align: left; color: #3EA99F; margin-bottom: 1px;'>Contact Us</h3>", unsafe_allow_html=True)

    loc_map, loc_text = st.columns(2)

    with loc_map:

    # Coordinates for Africa's Talking HQ
        location = [-1.2921, 36.7765]

        # Create the folium map
        m = folium.Map(location=location, zoom_start=12)

        folium.Marker(
            location,
            popup="VaaSmart HQ",
            tooltip="Click for more info",
            icon=folium.Icon(color="blue", icon="info-sign"),
            ).add_to(m)

        st_folium(m, width=900, height=300)


    with loc_text:
        st.write('')
        st.write('')
        st.write("<h6 style='text-align: left; margin-bottom: 1px;'>🏢 Apple Cross 23 - Lavington</h6>", unsafe_allow_html=True)
        st.write("<h6 style='text-align: left; margin-bottom: 1px;'>📬 P.O. Box 00200</h6>", unsafe_allow_html=True)
        st.write("<h6 style='text-align: left; margin-bottom: 1px;'>📌 Nairobi, Kenya</h6>", unsafe_allow_html=True)
        st.write("<h6 style='text-align: left; margin-bottom: 1px;'>📞 Tel: +254 71234 5678</h6>", unsafe_allow_html=True)
        st.write("<h6 style='text-align: left; margin-bottom: 1px;'>📧 Email: info@echominds.africa</h6>", unsafe_allow_html=True)
