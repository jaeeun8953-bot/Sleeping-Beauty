from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="NERI · 꿈결의 바다", page_icon="🌅", layout="wide", initial_sidebar_state="collapsed")
st.markdown('''<style>
.stApp {background:#152b33;}
[data-testid="stMainBlockContainer"] {padding:0!important;max-width:100%!important;}
[data-testid="stVerticalBlock"] {gap:0!important;}
[data-testid="stMainBlockContainer"] iframe {width:100%!important;height:100svh!important;border:0;display:block;}
[data-testid="stHeader"] {background:transparent;}
</style>''', unsafe_allow_html=True)

# Read from the repository directory on every run. No cached HTML or embedded payload.
beach_path = Path(__file__).resolve().parent / "neri_beach_castle.html"
if not beach_path.is_file():
    st.error("해변 파일이 없어요. GitHub에서 app.py와 같은 폴더에 neri_beach_castle.html을 올려주세요.")
    st.code(str(beach_path))
    st.stop()

try:
    html = beach_path.read_text(encoding="utf-8")
    if 'data-mold="triangle"' not in html:
        st.warning("모래성 파일 내용이 맞지 않아요. neri_beach_castle.html을 확인해주세요.")
    components.html(html, height=800, scrolling=False)
except Exception as error:
    st.error("해변을 여는 중 오류가 발생했어요.")
    st.exception(error)
