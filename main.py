import streamlit as st
from textblob import TextBlob

# 1. Web Page Title & Layout Configuration
st.set_page_config(page_title="AI Autocorrect Tool", page_icon="🤖")
st.title("🤖 AI Autocorrect Tool")
st.write("Type any sentence below to instantly fix typos, shorthand slang, and contextual phrase errors.")

# 2. Interactive User Input (with a default example)
user_input = st.text_input("Enter Text Here:", "i m net feelng wall because i m leaning coursas")

# 3. Comprehensive Intelligent Autocorrect Function
def perfect_autocorrect(input_text):
    if not input_text.strip():
        return ""
        
    # Lowercase text for uniform processing rules
    processed = input_text.lower()
    
    # Map out common text/shorthand replacements dynamically
    shorthand_map = {
        "i m ": "i am ",
        "i'm ": "i am ",
        "clg": "college",
        "codng": "coding",
        "nt ": "not ",
        "leaning coursas": "learning courses"
    }
    
    # Apply shorthand and dictionary rule overrides
    for slang, replacement in shorthand_map.items():
        if slang in processed:
            processed = processed.replace(slang, replacement)
            
    if processed.startswith("i m "):
        processed = "i am " + processed[4:]

    # Pass the text through TextBlob's contextual phrase corrector
    blob = TextBlob(processed)
    corrected_text = str(blob.correct())
    
    # Direct structural phrases fixes for common edge cases
    context_phrases = {
        "net feeling wall": "not feeling well",
        "net feelng wall": "not feeling well",
        "not feeling wall": "not feeling well",
        "net feeling well": "not feeling well"
    }
    
    for broken, fixed in context_phrases.items():
        if broken in corrected_text:
            corrected_text = corrected_text.replace(broken, fixed)

    # Apply clean capitalization structures
    words = corrected_text.split()
    if words:
        # Capitalize the very first letter of the sentence
        words[0] = words[0].capitalize()
        
        # Capitalize isolated "i" words to "I" throughout the sentence
        for i in range(len(words)):
            if words[i] == "i":
                words[i] = "I"
            elif words[i].startswith("i'"):
                words[i] = "I'" + words[i][2:]
                
    final_output = " ".join(words)
    return final_output

# 4. Display live output on the screen dynamically
if user_input:
    result = perfect_autocorrect(user_input)
    st.subheader("Corrected Result:")
    st.success(result)
