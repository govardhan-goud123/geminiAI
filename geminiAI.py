import streamlit as st
from google import genai

st.set_page_config(
    page_title="Gemini AI Chat",
    page_icon="✨",
    layout="centered"
)

# CSS
st.markdown("""
<style>
.stApp {
    background-color: #101426;
    color: white;
}
.block-container {
    max-width: 850px;
    padding-top: 2rem;
}
.title {
    text-align: center;
    padding: 25px;
    border-radius: 15px;
    background: linear-gradient(120deg, #202b55, #493b79);
    margin-bottom: 25px;
}
.title h1 {
    color: white;
}
.title p {
    color: #d0d5f5;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="title">
    <h1>✨ Gemini AI Assistant</h1>
    <p>Powered by Google Gemini 3.6 Flash</p>
</div>
""", unsafe_allow_html=True)

# Gemini Client
client = genai.Client()

# Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
prompt = st.chat_input("Ask Gemini anything...")

if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        try:
            with st.spinner("Gemini is thinking..."):

                interaction = client.interactions.create(
                    model="gemini-3.6-flash",
                    input=prompt
                )

            answer = interaction.output_text

            st.markdown(answer)

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

        except Exception as e:
            st.error(f"Error: {e}")
            st.session_state.messages.pop()