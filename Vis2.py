### Assignment No 6 ###
"""
Assignment Title: Implement and visualize Dependency Parsing of Textual Input
using Stanford CoreNLP and Spacy library
"""

import spacy
from spacy import displacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# New text for dependency parsing
multiline_text = """
Artificial Intelligence (AI) is transforming the way we interact with technology. 
It enables machines to learn from data, make predictions, and perform tasks that previously required human intelligence. 
With advancements in machine learning and deep learning, AI is being applied across healthcare, finance, and transportation industries.
"""

# Process the text
doc = nlp(multiline_text)

# Print token-level dependency information
for token in doc:
    print(f"TOKEN: {token.text}")
    print(f"POS Tag: {token.tag_}")
    print(f"Head Word: {token.head.text}")
    print(f"Dependency: {token.dep_}")
    print("=====")

# Visualize dependency parse in a browser
# auto_select_port=True ensures it picks a free port if 5000 is in use
displacy.serve(doc, style="dep", auto_select_port=True)
