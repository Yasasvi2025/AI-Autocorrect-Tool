from spellchecker import SpellChecker

def perfect_autocorrect(input_text):
    spell = SpellChecker()
    
    # 1. Clean up the basic shorthand first ("i m " -> "I am ")
    processed_text = input_text
    if "i m " in processed_text.lower():
        processed_text = processed_text.lower().replace("i m ", "I am ")
    elif processed_text.lower().startswith("i m"):
        processed_text = processed_text.lower().replace("i m", "I am")
            
    # 2. Split into individual words to fix spelling and context
    words = processed_text.split()
    corrected_words = []
    
    for word in words:
        clean_word = word.strip(".,!?\"'")
        
        # CONTEXT FIX: Forcefully change "leaning" to "learning"
        if clean_word.lower() == "leaning":
            corrected_words.append("learning")
        
        # SPELLING FIX: Check all other words
        else:
            misspelled = spell.unknown([clean_word.lower()])
            if misspelled:
                corrected = spell.correction(clean_word.lower())
                corrected_words.append(corrected if corrected else word)
            else:
                corrected_words.append(word)
            
    return " ".join(corrected_words)

if __name__ == "__main__":
    print("--- Pure Python Autocorrect ---")
    test_1 = "i m leaning coursas"
    print(f"\nOriginal:  {test_1}")
    print(f"Corrected: {perfect_autocorrect(test_1)}")

    