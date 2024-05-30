import streamlit as st
import json
import difflib

# Load the data from the JSON file
dat = json.load(open("data.json"))

# CSS to hide the scrollbar and style elements
st.markdown("""
    <style>
    .noscroll {
        overflow: hidden;
        white-space: wrap;
        text-overflow: ellipsis;
    }
    </style>
    """, unsafe_allow_html=True)

# Function to find the meaning of the word
def findMeaning(word, i):
    if word in dat:
        return dat[word]
    elif word.lower() in dat:
        return dat[word.lower()]
    elif word.upper() in dat:
        return dat[word.upper()]
    elif word.title() in dat:
        return dat[word.title()]
    elif len(difflib.get_close_matches(word, dat.keys())) > i:
        suggestion = difflib.get_close_matches(word, dat.keys())[i]
        st.text(f"Did you mean {suggestion}?")
        decide = st.text_input("Confirm your choice (Yes/No):", key=f"decide_{i}")
        if decide.lower() == 'yes':
            return findMeaning(suggestion, 0)
        elif decide.lower() == 'no':
            return findMeaning(word, i + 1)
        else:
            st.text("Please respond with 'Yes' or 'No'.")
            return None
    else:
        return "No matches found."

# Title and subtitle of the application
st.markdown("""
    <h1 style='text-align: center; background-color: #ADD8E6; padding: 10px; border-radius: 10px;'>📖 VerbaVis 📖</h1><br>
    """, unsafe_allow_html=True)
re = st.button("Reload",key="reload")
if re:
    st.experimental_rerun()

st.markdown("### ***Enter the word:***")

# Text input for the word search
word = st.text_input("", placeholder='Your word to search')
if word:
    meaning = findMeaning(word, 0)
    if meaning:
        if isinstance(meaning, list):
            st.text("The possible definitions are:")
            for i in meaning:
                st.markdown(f'<div class="noscroll">{i}</div>', unsafe_allow_html=True)
                st.text("\n")
        else:
            st.markdown(f'<div class="noscroll">{meaning}</div>', unsafe_allow_html=True)
            st.text("\n")
    else:
        st.text("No matches found.")
