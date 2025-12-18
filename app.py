import random
import datetime

# --- SETTINGS ---
today = datetime.date.today()
random.seed(today.toordinal())

# --- DATA ---
words = [
    "Ambition (Rhymes: Condition, Ignition)",
    "Monumental (Rhymes: Fundamental, Rental)",
    "Sacrifice (Rhymes: Paradise, Cold as ice)",
    "Atmosphere (Rhymes: Last year, No fear)",
    "Gravity (Rhymes: Depravity, Tragedy)",
    "Resilience (Rhymes: Brilliance, Millions)",
    "Vendetta (Rhymes: Go get a, Better, Letter)"
]

sentences = [
    "The city was loud, but his thoughts were louder.",
    "I watched the bridge burn and used the light to read.",
    "Empty pockets but a head full of blueprints.",
    "They told me to wait in line, so I built a new door.",
    "Silence speaks volumes when you listen to the frequency.",
    "The finish line keeps moving every time I get close."
]

motivation = [
    "Amateurs wait for inspiration. Pros get up and go to work.",
    "Your favorite rapper started with zero fans. Keep going.",
    "Flow is temporary. Skill is permanent.",
    "Don't edit while you write. Let the ink bleed first.",
    "If it was easy, everyone would do it. That's your advantage."
]

# --- LOGIC ---
daily_word = random.choice(words)
daily_sentence = random.choice(sentences)
daily_motivation = random.choice(motivation)
date_display = today.strftime("%B %d, %Y")

# --- DISPLAY ---
print("\n" + "="*40)
print(f"📅 DATE: {date_display}")
print("="*40)
print(f"\n🎤 RAP WORD: {daily_word}")
print(f"\n📝 PROMPT:   {daily_sentence}")
print(f"\n🔥 DRIVE:    {daily_motivation}")
print("\n" + "-"*40)

# --- SAVE ---
with open("rap_journal.txt", "a", encoding="utf-8") as f:
    f.write(f"[{date_display}] Word: {daily_word}\nPrompt: {daily_sentence}\n\n")

input("\n✅ Saved to rap_journal.txt\nPress Enter to close...")