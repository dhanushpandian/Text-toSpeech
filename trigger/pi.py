import socketio
import subprocess

sio = socketio.Client()

@sio.event
def connect():
    print('Connected to Node.js server')

@sio.event
def transaction(amount):
    print('Received transaction signal with amount:', amount)
    subprocess.run(['python', 'ttl.py', str(amount)])  # Call the text-to-speech script

@sio.event
def disconnect():
    print('Disconnected from Node.js server')

if __name__ == "__main__":
    sio.connect('http://localhost:3000')  # Replace with your Node.js server IP
    sio.wait()
