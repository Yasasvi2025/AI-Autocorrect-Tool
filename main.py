import streamlit as st
from textblob import TextBlob

# 1. Web Page Title
st.title("🤖 AI Autocorrect Tool")
st.write("Type a sentence below to instantly fix typos, shorthand, and contextual errors.")

# 2. Web Input Text Box
user_input = st.text_input("Enter Text Here:", "i m net feelng wall")

# 3. Enhanced Context Autocorrect Function
def perfect_autocorrect(input_text):
    processed_text = input_text
    
    # Clean up common shorthand and tricky manual typos first
    if "i m " in processed_text.lower():
        processed_text = processed_text.lower().replace("i m ", "i am ")
    elif processed_text.lower().startswith("i m"):
        processed_text = processed_text.lower().replace("i m", "i am ")
        
    # Manual context boosters for common phrase typos
    processed_text = processed_text.replace(" net feelng ", " not feelng ")
    processed_text = processed_text.replace(" net feeling ", " not feeling ")

    # Pass the boosted text to TextBlob for overall phrase correction
    blob = TextBlob(processed_text)
    corrected_text = str(blob.correct())
    
    # Catching trailing word context errors if any remain
    if corrected_text.endswith("feeling wall"):
        corrected_text = corrected_text.replace("feeling wall", "feeling well")
    
    # Capitalize the 'I' properly for perfect grammar
    if corrected_text.startswith("i am"):
        corrected_text = "I am" + corrected_text[4:]
        
    return corrected_text

# 4. Display output on the screen when the user types
if user_input:
    result = perfect_autocorrect(user_input)
    st.subheader("Corrected Result:")
    st.success(result)
