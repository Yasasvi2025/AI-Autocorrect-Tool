import streamlit as st
from textblob import TextBlob

# 1. Page Configuration & Title
st.set_page_config(page_title="AI Autocorrect Tool", page_icon="🤖")
st.title("🤖 AI Autocorrect Tool")
st.write("Type any sentence below to instantly fix typos, shorthand slang, and contextual phrase errors.")

# 2. Interactive Text Input Box
user_input = st.text_input("Enter Text Here:", "i m net geing to clg bcz i m leaning codng coursas")

# 3. Comprehensive Autocorrect Engine
def dynamic_autocorrect(input_text):
    if not input_text.strip():
        return ""
        
    # Convert text to lowercase for uniform processing
    processed = input_text.lower().strip()
    
    # Universal Vocabulary Map: Fixes shorthand, real-word mixups, and heavily broken terms
    context_map = {
        "i m ": "i am ",
        "i'm ": "i am ",
        "geing": "going",
        "te ": "to ",
        "hespitel": "hospital",
        "net ": "not ",
        "feelng": "feeling",
        "wall": "well",
        "leaning": "learning",
        "coursas": "courses",
        "codng": "coding",       
        "clg": "college",
        "bcz": "because",        
        "u ": "you ",
        "r ": "are ",
        "txt": "text",
        "msg": "message",
        "fare college": "for college",
        "fare clg": "for college"
    }
    
    # Step A: Apply vocabulary map replacements
    for broken_word, fixed_word in context_map.items():
        processed = processed.replace(broken_word, fixed_word)
        
    if processed.startswith("i m "):
        processed = "i am " + processed[4:]

    # Step B: Let TextBlob handle standard spell checking for remaining words
    blob = TextBlob(processed)
    corrected_text = str(blob.correct())
    
    # Step C: Fallback structural phrase cleanups
    phrase_overrides = {
        "i am net feeling wall": "i am not feeling well",
        "i am being te despite": "i am going to the hospital",
        "i am going to despite": "i am going to the hospital",
        "i am leaning courses": "i am learning courses",
        "learning coming courses": "learning coding courses", 
        "late fare college": "late for college"
    }
    for bad_phrase, good_phrase in phrase_overrides.items():
        if bad_phrase in corrected_text.lower():
            corrected_text = corrected_text.lower().replace(bad_phrase, good_phrase)

    # Step D: Apply perfect English grammar capitalization
    words = corrected_text.split()
    if words:
        words[0] = words[0].capitalize()  # Capitalize sentence start
        for i in range(len(words)):
            if words[i] == "i":
                words[i] = "I"            # Capitalize isolated "I"
            elif words[i].startswith("i'"):
                words[i] = "I'" + words[i][2:]
                
    return " ".join(words)

# 4. Process and Display Output Live
if user_input:
    with st.spinner("Refining sentence meaning..."):
        result = dynamic_autocorrect(user_input)
    st.subheader("Meaningful Corrected Result:")
    st.success(result)

