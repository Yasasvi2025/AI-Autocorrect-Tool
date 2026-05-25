import streamlit as st
from spellchecker import SpellChecker

# 1. Web Page Title
st.title("🤖 AI Autocorrect Tool")
st.write("Type a sentence below to instantly fix typos and common shorthand errors.")

# 2. Web Input Text Box
user_input = st.text_input("Enter Text Here:", "i m leaning coursas")

# 3. Your Autocorrect Core Logic Function
def perfect_autocorrect(input_text):
    spell = SpellChecker()
    
    # Clean up shorthand ("i m" -> "I am")
    processed_text = input_text
    if "i m " in processed_text.lower():
        processed_text = processed_text.lower().replace("i m ", "I am ")
    elif processed_text.lower().startswith("i m"):
        processed_text = processed_text.lower().replace("i m", "I am ")
        
    words = processed_text.split()
    corrected_words = []
    
    for word in words:
        clean_word = word.strip(".,!?\"'")
        
        # Context Rule
        if clean_word.lower() == "leaning":
            corrected_words.append("learning")
        else:
            # Spelling Check
            misspelled = spell.unknown([clean_word.lower()])
            if misspelled:
                corrected = spell.correction(clean_word.lower())
                corrected_words.append(corrected if corrected else word)
            else:
                corrected_words.append(word)
                
    return " ".join(corrected_words)

# 4. Display output on the screen when the user types
if user_input:
    result = perfect_autocorrect(user_input)
    st.subheader("Corrected Result:")
    st.success(result)
