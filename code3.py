import streamlit as st
from textblob import TextBlob

# 1. Web Page Title
st.title("🤖 AI Autocorrect Tool")
st.write("Type a sentence below to instantly fix typos, shorthand, and contextual errors.")

# 2. Web Input Text Box
user_input = st.text_input("Enter Text Here:", "i m net feelng wall")

# 3. TextBlob Context Autocorrect Function
def perfect_autocorrect(input_text):
    # Fix basic shorthand spacing first
    processed_text = input_text
    if "i m " in processed_text.lower():
        processed_text = processed_text.lower().replace("i m ", "i am ")
    elif processed_text.lower().startswith("i m"):
        processed_text = processed_text.lower().replace("i m", "i am ")

    # Use TextBlob to analyze the whole phrase context
    blob = TextBlob(processed_text)
    corrected_text = str(blob.correct())
    
    # Capitalize the 'I' for proper grammar structure
    if corrected_text.startswith("i am"):
        corrected_text = "I am" + corrected_text[4:]
        
    return corrected_text

# 4. Display output on the screen when the user types
if user_input:
    result = perfect_autocorrect(user_input)
    st.subheader("Corrected Result:")
    st.success(result)
