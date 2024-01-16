import socketio
import subprocess
import sys
import pyttsx3

# Initialize socket.io client
sio = socketio.Client()

# Initialize text-to-speech engine
def text_to_speech(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

# Socket.io event handlers
@sio.event
def connect():
    print('Connected to Node.js server')

@sio.event
def transaction(amount):
    print('Received transaction signal with amount:', amount)
    try:
        # Perform text-to-speech
        text_to_speech(str(amount))
    except Exception as e:
        print(f"Error during text-to-speech conversion: {e}")

@sio.event
def disconnect():
    print('Disconnected from Node.js server')

if __name__ == "__main__":
    # Connect to the Node.js server
    sio.connect('http://192.168.89.1:3000')

    # Wait for events
    sio.wait()
