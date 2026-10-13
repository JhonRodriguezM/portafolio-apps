from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="KNN — ¿De qué grupo soy?", page_icon="🎯", layout="wide")

st.title("KNN — ¿De qué grupo soy?")
st.caption("Sesión 12 · Clasificación KNN. App interactiva compartida en clase.")

html = (Path(__file__).parent.parent / "html" / "knn-de-que-grupo-soy.html").read_text(encoding="utf-8")
components.html(html, height=1700, scrolling=True)
