import sys
import pyttsx3

def text_to_speech(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 ttl.py <message>")
        sys.exit(1)

    message = sys.argv[1]
    text_to_speech(message)
