import streamlit as st
import random
import datetime

# --- HIDE ALL WEB INTERFACE CLUTTER ---
st.set_page_config(page_title="Daily Bars", page_icon="🎤")
hide_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 1rem; padding-bottom: 1rem;}
    </style>
    """
st.markdown(hide_style, unsafe_allow_html=True)

# --- DATA BANK ---
words = [
    {"word": "Obsession", "rhymes": "Possession, Progression, Lesson, Profession"},
    {"word": "Titanium", "rhymes": "Cranium, Uranium, Stadium, Geranium"},
    {"word": "Mirage", "rhymes": "Garage, Collage, Sabotage, Barrage"},
    {"word": "Renaissance", "rhymes": "Response, Sconce, Nonce, Reconnaissance"},
    {"word": "Velocity", "rhymes": "Ferocity, Atrocity, Reciprocity"},
    {"word": "Atmosphere", "rhymes": "Last year, Frontier, Revere, Idea"},
    {"word": "Sanctuary", "rhymes": "January, Cemetery, Visionary, Statutory"},
    {"word": "Calamity", "rhymes": "Humanity, Vanity, Insanity, Profanity"},
    {"word": "Labyrinth", "rhymes": "Absinthe, Hyacinth, Platinum (slant)"},
    {"word": "Paradox", "rhymes": "Narrative, Scare of, Pair of, Air ducts"},
    {"word": "Metaphor", "rhymes": "Step war, Better for, Get more, Legend lore"},
    {"word": "Frequency", "rhymes": "Recently, Decently, Sequencing, Deep in the"},
    {"word": "Dynasty", "rhymes": "Majesty, Strategy, Tragedy, Honestly"},
    {"word": "Anarchy", "rhymes": "Hierarchy, Panarchy, Monarchally"},
    {"word": "Prophecy", "rhymes": "Policy, Quality, Honestly, Oddity"},
    {"word": "Eclipse", "rhymes": "Scripts, Lips, Chips, Apocalypse"},
    {"word": "Blueprint", "rhymes": "Footprint, New hint, True tint, Cool mint"},
    {"word": "Havoc", "rhymes": "Savage, Average, Baggage, Damage"},
    {"word": "Revenge", "rhymes": "Stonehenge, Unbend, Depend, Offend"},
    {"word": "Infamous", "rhymes": "Ignorance, Synchronous, Instances, Distances"},
    {"word": "Pressure", "rhymes": "Fresher, Treasure, Measure, Professor"},
    {"word": "Legacy", "rhymes": "Ecstasy, Jealousy, Embassy, Tendency"},
    {"word": "Concrete", "rhymes": "On beat, Street, Elite, Complete"},
    {"word": "Sovereign", "rhymes": "Governing, Hovering, Discovering"},
    {"word": "Vandalize", "rhymes": "Scandalize, Analyze, Standardize"},
    {"word": "Miracle", "rhymes": "Lyrical, Empirical, Spherical, Satirical"},
    {"word": "Paranoia", "rhymes": "Destroy ya, Lawyer, Employer, Top-tier"},
    {"word": "Vibration", "rhymes": "Location, Nation, Patient, Elevation"},
    {"word": "Adrenaline", "rhymes": "Medicine, Genuine, Better than, Skeleton"},
    {"word": "Ambition", "rhymes": "Ignition, Partition, Competition, Nutrition"},
    {"word": "Anatomy", "rhymes": "Academy, Strategy, Mastery, Gravity"},
    {"word": "Catastrophe", "rhymes": "Philosophy, Atrophy, Apostrophe, Modesty"},
    {"word": "Chameleon", "rhymes": "Million, Civilian, Pavilion, Billion"},
    {"word": "Criminal", "rhymes": "Subliminal, Minimal, Original, Digital"},
    {"word": "Alchemy", "rhymes": "Strategy, Majesty, Anatomy, Faculty"},
    {"word": "Midnight", "rhymes": "Big fight, Street light, Sit tight, This height"},
    {"word": "Outcast", "rhymes": "Doubt fast, Mouth past, South blast, Now last"},
    {"word": "Victory", "rhymes": "History, Mystery, Slippery, Ministry"}
]

sentences = [
    "The city was loud, but his thoughts were louder.",
    "Empty pockets but a head full of blueprints.",
    "The finish line keeps moving every time I get close.",
    "I'm writing chapters in a book they'll never read.",
    "The static on the radio sounded like a warning.",
    "I traded my shadow for a chance to stand in the light.",
    "The throne is empty, but the room is full of wolves.",
    "I found the key, but they changed the lock yesterday.",
    "Concrete flowers growing through the cracks of the curb.",
    "The ink is heavy when the story is light.",
    "Neon lights flickering like a heartbeat in the rain.",
    "Silence is the loudest sound in a room full of fakes.",
    "I built a bridge out of the stones they threw at me.",
    "Buried the past but the ghost keeps digging it up.",
    "The wolves don't bark, they wait for you to sleep.",
    "The puzzle is finished, but there’s one piece missing."
]

motivation = [
    "Amateurs wait for inspiration. Pros get to work.",
    "Your first draft is allowed to be bad. Just finish it.",
    "Consistency beats talent every single time.",
    "The booth is your therapist. Be honest with the mic.",
    "A page a day is a book a year. Don't stop.",
    "Your future self is counting on you right now.",
    "Focus on the output, not the applause.",
    "Don't stop when you're tired; stop when you're done."
]

# --- SEED LOGIC ---
today = datetime.date.today()
random.seed(today.toordinal())

daily_word = random.choice(words)
daily_sentence = random.choice(sentences)
daily_quote = random.choice(motivation)

# --- WIDGET VIEW ---
st.title(f"🎤 {daily_word['word'].upper()}")
st.markdown(f"**Rhymes:** {daily_word['rhymes']}")
st.divider()
st.info(f"📝 {daily_sentence}")
st.warning(f"🔥 {daily_quote}")
st.write("---END---")
