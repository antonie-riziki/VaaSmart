import streamlit as st 



reg_page = st.Page("./pgs/registration.py", title="register", icon=":material/person_add:")
signin_page = st.Page("./pgs/signin.py", title="sign in", icon=":material/login:")
home_page = st.Page("./pgs/main.py", title="home page", icon=":material/home:")
closet_page = st.Page("./pgs/closet.py", title="closet IQ", icon=":material/dry_cleaning:")
roast_page = st.Page("./pgs/roast.py", title="drip roast", icon=":material/theater_comedy:")
chatbot_page = st.Page("./pgs/chatbot.py", title="chatbot", icon=":material/chat:")



pg = st.navigation([reg_page, signin_page, home_page, closet_page, roast_page, chatbot_page])

st.set_page_config(
    page_title="Vaa Smart",
    page_icon="👗",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.echominds.africa',
        'Report a bug': "https://www.echominds.africa",
        'About': """
        VaaSmart is an intelligent fashion-tech platform designed to revolutionize the way Kenyans engage with clothing and style. Rooted in local culture and powered by 
        technology, VaaSmart helps users make smarter wardrobe choices by combining personalized fashion recommendations, local weather insights, and sustainable style tips. 
        Whether you're a fashion lover, a mitumba vendor, or a local designer, VaaSmart empowers you with tools to explore trends, discover culturally inspired outfits, and shop or 
        style consciously.
        
        By bridging the gap between innovation and tradition, VaaSmart supports Kenya’s growing fashion industry with data-driven insights, virtual try-ons, and a digital 
        marketplace that connects creators and consumers. Our mission is to promote fashion that is smart, inclusive, and future-ready."""
    }
)

pg.run()



