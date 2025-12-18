import streamlit as st
import random
import datetime

st.set_page_config(page_title="Daily Bars", page_icon="🎤")

# --- 1. THE RHYME BANK ---
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
    {"word": "Beggars", "rhymes": "Checkers, Vectors, Sectors, Protectors"},
    {"word": "Ghostwriter", "label": "No bias", "rhymes": "Lighter, Fighter, Exciter, Igniter"},
    {"word": "Hollow", "rhymes": "Follow, Swallow, Apollo, Marshmallow"},
    {"word": "Iceberg", "rhymes": "Nice word, Life heard, Right turn, White bird"},
    {"word": "Jigsaw", "rhymes": "Big draw, Quick claw, Brick wall, This raw"},
    {"word": "Kingpin", "rhymes": "Think thin, Ink pen, Big win, Sink in"},
    {"word": "Midnight", "rhymes": "Big fight, Street light, Sit tight, This height"},
    {"word": "Nightmare", "rhymes": "Right there, Flight fare, Light air, Might care"},
    {"word": "Outcast", "rhymes": "Doubt fast, Mouth past, South blast, Now last"},
    {"word": "Phantom", "rhymes": "Ransom, Handsome, Expansion, Mansion"},
    {"word": "Quickstand", "rhymes": "Kickstand, Big hand, Sick band, This land"},
    {"word": "Rebel", "rhymes": "Level, Devil, Metal, Special"},
    {"word": "Soulmate", "rhymes": "Whole state, Cold plate, Gold gate, Roll late"},
    {"word": "Tattoo", "rhymes": "Bad move, Fact too, Back to, That view"},
    {"word": "Umbrella", "rhymes": "Stella, Fella, Dweller, Stellar"},
    {"word": "Victory", "rhymes": "History, Mystery, Slippery, Ministry"}
]

# --- 2. STORY STARTERS (50+) ---
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
    "He spoke in riddles but lived in the truth.",
    "The map led to a place that doesn't exist anymore.",
    "Silence is the loudest sound in a room full of fakes.",
    "Gold chains couldn't hold the weight of his regret.",
    "The clock stopped ticking, but time kept moving.",
    "Streetlights acting like spotlights for the broken.",
    "I built a bridge out of the stones they threw at me.",
    "The penthouse view couldn't hide the basement secrets.",
    "He carried the world on his shoulders but never felt the weight.",
    "One hand on the Bible, the other on the trigger.",
    "The echo in the hallway told a story he forgot.",
    "Buried the past but the ghost keeps digging it up.",
    "The rain washed the blood off but not the memory.",
    "I’m chasing ghosts in a city that’s already dead.",
    "The mirror looked back and didn't recognize the face.",
    "Every bridge I cross, I light a match behind me.",
    "A king with no kingdom is just a man with a crown.",
    "The whispers in the alley became a roar in the booth.",
    "Traded the sunshine for a life in the spotlight.",
    "They promised paradise but gave us a parking lot.",
    "The diary was empty, but the scars were full of ink.",
    "I heard the truth in a lie he told ten years ago.",
    "Walking on water until I realized I could swim.",
    "The wolves don't bark, they wait for you to sleep.",
    "I sold my soul for a dream I can't even remember.",
    "The wind carries secrets that the mountains won't tell.",
    "Blood on the leaves, but the roots are still pure.",
    "He won the war but lost the reason he was fighting.",
    "I’m the author of a tragedy I haven't finished yet.",
    "They look at the watch but they don't see the time.",
    "The ocean is deep, but my lungs are getting stronger.",
    "Heaven is a mile away, but the road is made of glass.",
    "I’m talking to God, but the devil is listening in.",
    "The check cleared, but the conscience is still pending.",
    "Everything I love is on the other side of a wall.",
    "I left my heart in a place I can never go back to.",
    "The shadow follows me even when the sun goes down.",
    "I’m a saint in the morning and a sinner at night.",
    "The puzzle is finished, but there’s one piece missing."
]

# --- 3. MOTIVATION (50+) ---
motivation = [
    "Amateurs wait for inspiration. Pros get to work.",
    "Your first draft is allowed to be bad. Just finish it.",
    "Consistency beats talent every single time.",
    "Don't write for the fans you have; write for the fans you want.",
    "The booth is your therapist. Be honest with the mic.",
    "A page a day is a book a year. Don't stop.",
    "They laughed at the vision because they couldn't see the lens.",
    "Greatness is just a series of small wins repeated daily.",
    "Flow is temporary. Technical skill is permanent.",
    "If you're the smartest person in the room, find a new room.",
    "Don't polish the diamond before you dig it out the dirt.",
    "Your struggles are just content for the next classic.",
    "Write like you're already famous and have something to lose.",
    "Every 'no' is just one step closer to a 'yes'.",
    "Pressure creates diamonds; it also bursts pipes. Choose.",
    "The pen is a weapon. Keep it sharp.",
    "Stop comparing your Chapter 1 to someone else's Chapter 20.",
    "The only difference between a dream and a goal is a deadline.",
    "If it doesn't challenge you, it won't change you.",
    "Work until your idols become your rivals.",
    "Success is the best revenge. Keep winning.",
    "You don't need a permission slip to be great.",
    "Don't let a bad day turn into a bad year.",
    "Your voice is the only thing they can't copy.",
    "The harder you work, the luckier you get.",
    "Silence the doubt with the sound of your grind.",
    "One verse today is better than zero verses tomorrow.",
    "Stay hungry, stay humble, but stay dangerous.",
    "The world doesn't owe you anything. Go take it.",
    "Don't count the days; make the days count.",
    "Comfort is the enemy of progress.",
    "Your future self is counting on you right now.",
    "Be so good they can't ignore you.",
    "Hustle until your bank account looks like a phone number.",
    "The grind includes Friday, Saturday, and Sunday.",
    "You can't have a million-dollar dream with a minimum-wage work ethic.",
    "Focus on the output, not the applause.",
    "A year from now, you’ll wish you started today.",
    "Fail forward. Every mistake is a lesson in rhythm.",
    "Keep your circle small and your vision big.",
    "Don't be afraid to start over. This time you’re starting with experience.",
    "The mic doesn't care about your excuses.",
    "Discipline is doing what needs to be done even when you don't feel like it.",
    "Your craft is a gift. Don't leave it unopened.",
    "Be the version of you that you needed when you were younger.",
    "The road to success is always under construction.",
    "Passion is the fuel, but work is the engine.",
    "Don't stop when you're tired; stop when you're done.",
    "Great things never came from comfort zones.",
    "Believe in your sauce even when nobody is tasting it."
]

# --- LOGIC ---
today = datetime.date.today()
random.seed(today.toordinal())

daily_word = random.choice(words)
daily_sentence = random.choice(sentences)
daily_quote = random.choice(motivation)

# --- UI ---
st.title("🎤 Daily Bars")
st.caption(f"Rap Tool v2.0 | {today.strftime('%A, %B %d')}")
st.divider()

st.header(f"Word: {daily_word['word'].upper()}")
st.info(f"💡 Rhymes: {daily_word['rhymes']}")

st.subheader("📝 Story Starter")
st.success(f"\"{daily_sentence}\"")

st.subheader("🔥 Mindset")
st.warning(f"\"{daily_quote}\"")

st.divider()
st.button("Refresh Page")
