
from __future__ import annotations

import streamlit as st 
import sys
import folium

from folium.plugins import MarkerCluster
from geopy.geocoders import Nominatim
from streamlit_folium import st_folium



sys.path.insert(1, './modules')
sys.path.insert(1, './image_generation')
# print(sys.path.insert(1, '../modules/'))


from dotenv import load_dotenv

load_dotenv()


from func import autogenerate_weekly_outfit, autogenerate_daily_outfit, generate_outfit_image, geocode_location, search_nearby_apparel_stores
from image_generation import google_image_generator



@st.dialog("Login")
def location_form():
    with st.form(key="user_location"):
        location_input = st.text_input("Enter your location (e.g., Nairobi, Kenya):")
        submit_location = st.form_submit_button("Search Stores")

    return location_input


st.markdown(
    """
    <div class=title>
        <div style=" justify-content: center;">
            <h1 style="text-align: center; padding: 5px; color: #F52887;">AI Mirror 👗</h1>
            <p style="text-align: center;">Styled by Tech – Worn by You</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.image('https://3dlook.ai/wp-content/uploads/2021/07/main.jpg', width=900)



st.subheader('7 Days of Style')

with st.form(key="weekly_outfit"):

    col21, col22, col23 = st.columns(3)


    with col21:
        wk_gender = st.selectbox('Gneder', ['Male', 'Female', 'Binary', 'Non-Binary', 'Prefer not to say'])
        outfit_style = st.multiselect('Outfit', ['Any', 'Casual', 'Vintage', 'Streewear', 'Artsy Fashion', 'Sporty', 'Formal', 'Classic', 'Dramatic', 'Minimalist', 'Old Money aesthetics'])

    with col22:
        body_type = st.selectbox('Body Type', ['Hourglass', 'Pear', 'Apple', 'Petite', 'Tall', 'Short', 'Plus-size', 'Oval','Diamond'])
        weekly_occassions = st.multiselect('Occassion', ['Office', 'Outdoor', 'Wedding', 'Funeral', 'Networking', 'Conferences', 'Festival', 'Corporate'])


    with col23:
        race = st.selectbox('Race', ['African', 'Asian', 'Black American', 'Latino', 'Caucasian', 'Red Indians', 'Hispanic', 'White American'])
        add_info = st.text_area('Additional Information...', value=None, height=115)




    weekly_submit_button = st.form_submit_button('Generate Weekly Outfit', use_container_width=True, type='primary', icon=":material/calendar_month:")


prompt_input = f"""
    
    You are a smart fashion assistant.

    Based on the following user details:
    - Gender: {wk_gender}
    - Body Type: {body_type}
    - Race: {race} style
    - Preferred Outfit Style: {outfit_style}
    - Weekly Occasion Context: {weekly_occassions}
    - Additional Info: {add_info}

    Generate a weekly outfit schedule in a table format with 3 columns:
    1. Day (start with Sunday)
    2. Specific Outfit Recommendation (actual clothing items)
    3. Occasion (describe where the outfit is appropriate based on the occasion input)

    Return only the table with no extra explanation.
    
    """


if weekly_submit_button:

    st.write(autogenerate_weekly_outfit(prompt_input))



st.subheader('Daily Drip')



col1, col2 = st.columns(2, border=True)

with col1:
    with st.form(key="ai-mirror", border=False):

        st.subheader("Tell us about your day:")

        col14, col15 = st.columns(2)
        col16, col17 = st.columns(2)

        with col14:
            daily_gender = st.selectbox('Gender', options=['Male', 'Female'])

        with col15:
            age_grp = st.selectbox('Age Group', options=['Teen', '20s', '30s', '40s', '50s', '>60s'])

        with col16:
            weather_update = st.selectbox('Season', ['Any', 'Winter', 'Summer', 'Autumn', 'Spring', 'Monsoon'])

        with col17:
            mood = st.selectbox('Mood', ['Elegant', 'Energetic', 'Happy','Lazy','Motivated','Romatic', 'Confident','Chill', 'Adventurous', 'Classy','Bold'])

        daily_occassions = st.selectbox("What's the occasion?", [
            "Casual", "Formal", "Wedding", "Work/Office", "Outdoor Event", "Party", "Religious Event", "Other"
        ])
        
        col11,col12, col13 = st.columns(3)
        
        with col11:
            date = st.date_input("What date is it?")

        with col12:
            start_time = st.time_input("Start time")

        with col13:
            end_time = st.time_input("End time")
        
        location = st.text_input("Where is it happening? (e.g. Nairobi CBD, Westlands, Mombasa, etc.)")

        dress_code = st.selectbox("Any specific dress code?", [
            "None", "Traditional", "Smart Casual", "Business Formal", "White Theme", "Cultural", "Custom"
        ])
        
        weather_preference = st.radio("Do you prefer to dress for the weather?", ["Yes", "No"])
        
        personal_style = st.multiselect("Describe your personal style", [
            "Chic", "Urban", "Bold Prints", "Minimalist", "Boho", "Vintage", "Modern African", "Streetwear"
        ])

        additional_notes = st.text_area("Anything else we should know? (optional)")



        daily_submit_button = st.form_submit_button('Submit', use_container_width=True, type='primary', icon=':material/screen_search_desktop:')



daily_prompt_input = f"""
    
    You are a smart professional fashion stylist. Please recommend a complete outfit based on the following

    - Gender: {daily_gender}
    - Body Type: {age_grp}
    - Race: {weather_update} style
    - Preferred Outfit Style: {mood}
    - Weekly Occasion Context: {daily_occassions}
    - Date & Time: {date} {start_time} {end_time}
    - Location: {location}
    - Dress Code: {dress_code}
    - Weather Preference: {weather_preference}
    - Personal Style: {personal_style}
    - Additional Info: {additional_notes}

    Provide a CONCISE outfit recommendaiton (max 200 words) in this structured format:

    **TOP:** [describe the top item]\n
    **BOTTOM:** [describe the top item]\n
    **OUTWEAR:** [if needed fo weather]\n
    **SHOES:** [describe shoes]\n
    **ACCESSORIES:** [1-2 key accessories]

    
    
    """



def simplify_outfit_description(detailed_outfit: str) -> str:
    lines = detailed_outfit.strip().split("\n")
    simplified_parts = []

    for line in lines:
        if ":" in line:
            label, description = line.split(":", 1)
            simplified_parts.append(description.strip().rstrip("."))

    # Join all parts into a visual-friendly sentence
    simplified_prompt = (
        "A modern African-inspired outfit featuring " +
        ", ".join(simplified_parts) +
        ". Fashion photography, realistic style."
    )

    return simplified_prompt


detailed_image_prompt = f"""
    Create a realistic image of a person specifically {daily_gender} in their {age_grp}, styled to reflect a {mood} mood. They are dressed appropriately for attending a 
    {daily_occassions} event happening today, with the outfit suitable for {weather_update} weather.

    Note: The Person MUST be {daily_gender}

    \n Below is the outfit \n\n

    """

with col2:

    if daily_submit_button:
        daily_outfit = autogenerate_daily_outfit(daily_prompt_input)

        st.markdown(daily_outfit)

        image_prompt = simplify_outfit_description(daily_outfit)
        # st.markdown(image_prompt)

        google_image_generator(image_prompt + "\nJust return the outfit with a person wearing it")

        google_image_generator(image_prompt + detailed_image_prompt)

        shop_outfit = st.button('Order Outfit', use_container_width=True, icon=":material/delivery_truck_bolt:", type="primary")


        if shop_outfit:
            get_location = location_form()
            apparel_keywords = ["fashion", "clothing", "apparel", "boutique", "clothes", "outfit", "wardrobe", "dress", "shirt", "pants", "shoes", "collection"]

            if get_location:
                coords = geocode_location(get_location)

                if coords:
                    lat, lon = coords
                    st.success(f"📍 Location found: {lat}, {lon}")

                    stores = search_nearby_apparel_stores(lat, lon, apparel_keywords)

                    if stores:
                        # --- Step 3: Plotting Map ---
                        st.subheader("🗺 Nearby Apparel Stores")
                        map_ = folium.Map(location=[lat, lon], zoom_start=13)
                        marker_cluster = MarkerCluster().add_to(map_)

                        store_list = []

                        for store in stores:
                            store_name = store.get('tags', {}).get('name', 'Unnamed Store')
                            store_lat = store.get('lat') or store.get('center', {}).get('lat')
                            store_lon = store.get('lon') or store.get('center', {}).get('lon')
                            if store_lat and store_lon:
                                folium.Marker(
                                    location=[store_lat, store_lon],
                                    popup=store_name,
                                    icon=folium.Icon(color='blue', icon='shopping-bag', prefix='fa')
                                ).add_to(marker_cluster)
                                store_list.append(store_name)

                        st_data = st_folium(map_, width=700, height=500)

                        # --- Step 4: Top Stores List ---
                        st.subheader("🏬 Top Apparel Shops Nearby")
                        for i, name in enumerate(store_list[:10], 1):
                            st.markdown(f"{i}. **{name}**")

                    else:
                        st.warning("No apparel stores found matching your query in this area.")
                else:
                    st.error("Could not geocode the location. Please check your input.")



# st.title("🧥 Apparel Store Finder")
# location_input = st.text_input("Enter your location (e.g., Nairobi, Kenya):")






