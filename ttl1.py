import pyttsx3


def text_to_speech(text):
    try:
        # Initialize the TTS engine
        engine = pyttsx3.init()

        # Set properties (optional)
        engine.setProperty('rate', 100)  # Speed of speech
        engine.setProperty('volume', 10)  # Volume level (0.0 to 1.0)

        # Convert the text to speech
        engine.say(text)

        # Wait for the speech to finish
        engine.runAndWait()

    except Exception as e:
        print(f"Error during text-to-speech: {e}")


if __name__ == "__main__":
    # Replace this text with the message you want to convert to speech
    message = "Recived , paytm rupees 100"

    # Call the text-to-speech function
    text_to_speech(message)
