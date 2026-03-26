import streamlit as st
import base64
from PyPDF2 import PdfReader

svg = '''<svg width="140" height="180" viewBox="0 0 140 180" xmlns="http://www.w3.org/2000/svg">
  <polygon points="0,0 96,0 140,44 140,180 0,180" fill="#fff" stroke="#e0e0e0" stroke-width="1" stroke-linejoin="round"/>
  <polygon points="96,0 140,44 96,44" fill="#f0f0f0"/>
  <line x1="96" y1="0" x2="140" y2="44" stroke="#e0e0e0" stroke-width="1"/>
  <rect x="16" y="60" width="108" height="8" rx="3" fill="#e8e8e8"/>
  <rect x="16" y="76" width="90" height="8" rx="3" fill="#e8e8e8"/>
  <rect x="16" y="92" width="100" height="8" rx="3" fill="#e8e8e8"/>
  <rect x="0" y="118" width="140" height="62" rx="6" fill="#E53935"/>
  <rect x="0" y="118" width="140" height="14" fill="#E53935"/>
  <text x="70" y="158" text-anchor="middle" font-family="Arial" font-size="22" font-weight="700" fill="#fff" letter-spacing="1">PDF</text>
</svg>'''

b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")

st.markdown(
    f'''
    <div style="display:flex; align-items:center; gap:12px;">
        <img src="data:image/svg+xml;base64,{b64}" width="40"/>
        <h1 style="margin:0;">PDF Text Extractor</h1>
    </div>
    ''',
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader("Upload a File", type= ["pdf"])

if uploaded_file is not None:

    reader = PdfReader(uploaded_file)

    text = ""
    
    for page in reader.pages:
        text += page.extract_text()

    st.subheader("Extracted Text")

    st.text_area("Pdf Text", text, height= 450)

