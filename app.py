import streamlit as st
import ollama
import fitz

# -----------------------------
# PAGE SETTINGS
# -----------------------------
st.set_page_config(
    page_title="Campus Guide",
    layout="wide"
)

# -----------------------------
# DARK THEME STYLING
# -----------------------------
st.markdown("""
<style>
body {
    background-color: #0E1117;
}

.hero-title {
    font-size: 64px;
    font-weight: 800;
    color: white;
}

.hero-sub {
    font-size: 22px;
    color: #D1D5DB;
    margin-top: 15px;
}

.stTextInput > div > div > input {
    background-color: #1F2937 !important;
    color: white !important;
    border-radius: 12px !important;
    padding: 14px !important;
    border: 1px solid #374151 !important;
}

.answer-box {
    background-color: #1F2937;
    padding: 25px;
    border-radius: 16px;
    margin-top: 25px;
    color: white;
    font-size: 17px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.4);
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HERO SECTION
# -----------------------------
col1, col2 = st.columns([1.3, 1])

with col1:
    st.markdown("<div class='hero-title'>Campus Guide</div>", unsafe_allow_html=True)
    st.markdown("<div class='hero-sub'>Your AI-powered campus information assistant.</div>", unsafe_allow_html=True)

with col2:
    st.image("campus.jpg", use_column_width=True)

st.markdown("---")

# -----------------------------
# LOAD PDF AUTOMATICALLY
# -----------------------------
pdf_path = "college_data.pdf"

doc = fitz.open(pdf_path)
text = ""

for page in doc:
    text += page.get_text()

doc.close()

# -----------------------------
# QUESTION SECTION
# -----------------------------
st.markdown("### Ask a Question")

query = st.text_input(" ")

if query:
    with st.spinner("Analyzing campus data..."):
        response = ollama.chat(
            model="mistral",
            messages=[
                {
                    "role": "user",
                    "content": f"Context:\n{text}\n\nQuestion: {query}"
                }
            ]
        )

    st.markdown(
        f"<div class='answer-box'>{response['message']['content']}</div>",
        unsafe_allow_html=True
    )