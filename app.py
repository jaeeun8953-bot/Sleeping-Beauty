from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="NERI · 꿈결의 바다", page_icon="🌅", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>
html, body, .stApp {background:#152b33;}
[data-testid="stHeader"], [data-testid="stToolbar"], footer {display:none!important;}
[data-testid="stMainBlockContainer"] {padding:0!important;max-width:100%!important;}
[data-testid="stMain"] {overflow:hidden;}
[data-testid="stVerticalBlock"] {gap:0!important;}
iframe[title="streamlit.components.v1.html"] {width:100%!important;height:100dvh!important;border:0;display:block;}
</style>""", unsafe_allow_html=True)

@st.cache_data(show_spinner=False)
def beach_html():
    return Path(__file__).with_name("beach.html").read_text(encoding="utf-8")

components.html(beach_html(), height=900, scrolling=False)
