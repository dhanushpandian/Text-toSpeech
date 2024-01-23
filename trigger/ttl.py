import sys
import pyttsx3

def text_to_speech(message):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Adjust the speech rate (you can experiment with different values)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)

    # Choose a voice (you can experiment with different voices)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Adjust the index as needed

    # Say the message
    engine.say(message)

    # Wait for the speech to finish
    engine.runAndWait()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 ttl.py <message>")
        sys.exit(1)

    message = sys.argv[1]
    text_to_speech(message)

# import sys
# import pyttsx3

# def text_to_speech(message):
#     engine = pyttsx3.init()
#     engine.say(message)
#     engine.runAndWait()

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: python3 ttl.py <message>")
#         sys.exit(1)

#     message = sys.argv[1]
#     text_to_speech(message)
