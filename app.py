import streamlit as st
import random

# A list of sample quotes
quotes = [
    "The best way to get started is to quit talking and begin doing. – Walt Disney",
    "Don’t let yesterday take up too much of today. – Will Rogers",
    "It’s not whether you get knocked down, it’s whether you get up. – Vince Lombardi",
    "If you are working on something exciting, it will keep you motivated. – Steve Jobs",
    "Success is not in what you have, but who you are. – Bo Bennett",
    "Happiness is not something ready made. It comes from your own actions. – Dalai Lama",
]

st.set_page_config(page_title="Random Quote Generator", page_icon="💬", layout="centered")

st.title("💬 Random Quote Generator")

if st.button("Generate Quote"):
    quote = random.choice(quotes)
    st.success(quote)
else:
    st.info("Click the button to generate a random quote!")
