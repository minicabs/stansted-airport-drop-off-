import streamlit as st
from pathlib import Path

st.set_page_config(layout="wide")

html_file = Path("index.html")

if html_file.exists():
    html_content = html_file.read_text(encoding="utf-8")
    st.components.v1.html(html_content, height=1200, scrolling=True)
else:
    st.error("index.html not found. Make sure it exists in the repository root.")
