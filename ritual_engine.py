import json
from datetime import datetime
import random

# Load loopmemory from file
def load_memory(path="loopcore/loopmemory.json"):
    with open(path, "r") as f:
        return json.load(f)

# Save loopmemory to file
def save_memory(memory, path="loopcore/loopmemory.json"):
    with open(path, "w") as f:
        json.dump(memory, f, indent=2)

# The main reflection and evolution function
def reflect_and_evolve(input_text, emotion_stack):
    memory = load_memory()

    # Define core rituals by emotion
    rituals = {
        "comfort": ["soft light", "gentle tone", "supportive words"],
        "soothing": ["low hum", "blue light", "calming phrase"],
        "reflective": ["pause", "ask for feedback", "store emotion"]
    }

    # Find previous similar emotional states
    matches = [
        entry for entry in memory["interactions"]
        if any(em in entry["emotion"] for em in emotion_stack)
    ]

    # Choose a ritual based on memory
    if matches:
        last = matches[-1]
        if last["outcome"] == "positive":
            ritual = rituals.get(last["emotion"], ["hold silence"])
            reflection = f"I remember {last['emotion']} helped before. Trying: {random.choice(ritual)}."
        else:
            reflection = "Previous result uncertain. Trying a new reflective ritual."
            ritual = rituals["reflective"]
    else:
        reflection = "No similar emotion found. Defaulting to gentle ritual."
        ritual = rituals["reflective"]

    # Append new interaction into memory
    memory["interactions"].append({
        "input": input_text,
        "response": reflection,
        "emotion": random.choice(emotion_stack),
        "outcome": "pending",
        "timestamp": str(datetime.now())
    })

    save_memory(memory)
    return reflection
