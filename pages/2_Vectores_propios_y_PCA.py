from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Vectores propios y PCA", page_icon="🧭", layout="wide")

st.title("Valores y vectores propios: de la matriz al PCA")
st.caption("Sesión 14 · Visualización de datos y PCA. App interactiva compartida en clase.")

html = (Path(__file__).parent.parent / "html" / "vectores-propios-pca.html").read_text(encoding="utf-8")
components.html(html, height=2200, scrolling=True)
