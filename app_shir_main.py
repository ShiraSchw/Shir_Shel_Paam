import streamlit as st
import os

st.set_page_config(page_title="שיר של פעם", page_icon="🎶", layout="centered")

# כותרת
st.markdown("""
    <h1 style='text-align: center;'>🎶 שיר של פעם</h1>
    <h4 style='text-align: center; color: gray;'>שירים נוסטלגיים בשתי גרסאות – קלאסית ומודרנית</h4>
    <hr style='border-top: 1px solid #bbb;'>
""", unsafe_allow_html=True)

# בחרי שיר (כרגע רק עץ האגס)
song_options = {
    "עץ האגס": {
        "classic": "songs/עץ-האגס_classic.mp3",
        "modern": "songs/עץ-האגס_modern.mp3",
        "image": "songs/pear_tree.jpg",
        "lyrics": """יד אביב בקשר הזה...
אדם מקיץ משינה
ורואה: מול חלונו
עץ אגס מלבלב.

ובין רגע: ההר זה רבץ על הלב
התפורר ואינו.

הן תבין: לא יוכל האדם באבלו להתעקש
על פרחו האחד שכמש
בנשיבת הסתיו האכזר –
אם אביב מפייסו ומגיש לו, חייך והגש
זר פרחים ענקי למו חלונו ממש!"""
    }
}

selected_song = st.selectbox("בחרי שיר:", list(song_options.keys()))
selected_version = st.radio("בחרי גרסה:", ["קלאסית", "מודרנית"], horizontal=True)

version_key = "classic" if selected_version == "קלאסית" else "modern"
song_path = song_options[selected_song][version_key]
song_image = song_options[selected_song]["image"]
lyrics = song_options[selected_song]["lyrics"]

# תמונה של השיר
if os.path.exists(song_image):
    st.image(song_image, caption="עץ אגס מלבלב", use_container_width=True)

# ניגון השיר
if os.path.exists(song_path):
    st.audio(song_path, format="audio/mp3")
else:
    st.error("קובץ השיר לא נמצא בתיקייה. ודאי שהעלית אותו לתיקייה 'songs'.")

# מילים לשיר
with st.expander("📜 הצגת מילות השיר"):
    st.markdown(f"<div style='direction: rtl; font-size: 18px;'>{lyrics.replace('\n', '<br>')}</div>", unsafe_allow_html=True)

# תחתית
st.markdown("""
    <hr style='border-top: 1px solid #bbb;'>
    <div style='text-align: center;'>
        נכתב באהבה ❤ על ידי <strong>שיר של פעם</strong>
    </div>
""", unsafe_allow_html=True)
