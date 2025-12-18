import streamlit as st
import random
import datetime
import requests
import base64

# --- GITHUB CONFIGURATION ---
# Replace with your actual Token you generated earlier
GITHUB_TOKEN = "YOUR_GITHUB_TOKEN_HERE" 
REPO_NAME = "Leanderschepers-star/daily-rap-app"
FILE_PATH = "daily_bars.txt"

# --- HIDE INTERFACE CLUTTER ---
st.set_page_config(page_title="Daily Bars", page_icon="🎤")
st.markdown("<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;} header {visibility: hidden;}</style>", unsafe_allow_html=True)

# --- DATA BANK (Keeping your lists) ---
words = [
    {"word": "Obsession", "rhymes": "Possession, Progression, Lesson, Profession"},
    {"word": "Titanium", "rhymes": "Cranium, Uranium, Stadium, Geranium"},
    {"word": "Mirage", "rhymes": "Garage, Collage, Sabotage, Barrage"},
    {"word": "Vandalize", "rhymes": "Scandalize, Analyze, Standardize"},
    # ... (Keep all your other words here)
]

sentences = [
    "The city was loud, but his thoughts were louder.",
    "Empty pockets but a head full of blueprints.",
    # ... (Keep all your other sentences here)
]

motivation = [
    "Amateurs wait for inspiration. Pros get to work.",
    "Consistency beats talent every single time.",
]

# --- SEED LOGIC ---
today = datetime.date.today()
random.seed(today.toordinal())

daily_word = random.choice(words)
daily_sentence = random.choice(sentences)
daily_quote = random.choice(motivation)

# --- NEW: GITHUB UPDATE FUNCTION ---
def sync_to_github(word, sentence):
    url = f"https://api.github.com/repos/{REPO_NAME}/contents/{FILE_PATH}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    
    # Get current file info
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        sha = r.json()['sha']
        
        # Format the text exactly as requested:
        # WORD: VANDALIZED
        # The city was loud.
