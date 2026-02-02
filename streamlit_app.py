import streamlit as st
from summarizer.openai_summarizer import OpenAISummarizer

# Page config
st.set_page_config(
    page_title="Smart Text Summarizer",
    page_icon="",
    layout="centered"
)

st.title("Smart Text Summarizer")
st.write("Summarize long text using AI with structured prompting.")

# Input text
text = st.text_area(
    "Enter text to summarize",
    height=250,
    placeholder="Paste your article, documentation, or notes here..."
)

# Summary type selection
summary_type = st.selectbox(
    "Select summary type",
    ["Short Summary", "Bullet Points", "Key Takeaways"]
)

# Button
if st.button("Summarize"):
    if not text.strip():
        st.warning("Please enter some text to summarize.")
    else:
        with st.spinner("Summarizing..."):
            summarizer = OpenAISummarizer()
            summary = summarizer.summarize(text, summary_type)

        st.subheader("Summary")
        st.write(summary)
