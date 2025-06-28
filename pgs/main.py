
from __future__ import annotations

import streamlit as st 
import sys



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






