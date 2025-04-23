# app.py
import streamlit as st

st.set_page_config(page_title="שיר של פעם", page_icon="🎵", layout="centered")

st.title("🎵 שיר של פעם")
st.write("אפליקציה שמנגנת שירים נוסטלגיים בשתי גרסאות – קלאסית ומודרנית.")

song = st.selectbox("בחרי שיר:", ["עץ האגס"])
version = st.radio("בחרי גרסה:", ["קלאסית", "מודרנית"])

file_name = f"songs/עץ-האגס_{'classic' if version == 'קלאסית' else 'modern'}.mp3"
try:
    st.audio(file_name, format="audio/mp3")
except FileNotFoundError:
    st.error("קובץ השיר לא נמצא. ודאי שהעלית אותו לתיקייה 'songs'.")

st.caption("נכתב באהבה על ידי ✨")