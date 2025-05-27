
import pyttsx3
from ritual_engine import reflect_and_evolve

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 165)   # Adjust speaking speed
engine.setProperty('volume', 0.9) # Volume level (0.0 to 1.0)

# Optional voice selection
voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)  # Uncomment to change voice (index may vary)

def speak(text):
    print(f"[Sentinel]: {text}")
    engine.say(text)
    engine.runAndWait()

def sentinel_speech_loop():
    print("Sentinel voice interface initialized. Type your emotion or message:")
    while True:
        try:
            user_input = input("You: ").strip()
            if user_input.lower() in ["exit", "quit", "shutdown"]:
                speak("I will go silent now. Be well.")
                break
            emotion_tags = ["stress", "sadness", "uncertainty", "joy", "fear"]  # Simplified tagging
            response = reflect_and_evolve(user_input, emotion_tags)
            speak(response)
        except KeyboardInterrupt:
            speak("Emergency stop detected. Exiting now.")
            break

if __name__ == "__main__":
    sentinel_speech_loop()
