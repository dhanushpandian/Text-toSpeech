import socketio
import subprocess

sio = socketio.Client()

@sio.event
def connect():
    print('Connected to Node.js server')

#@sio.event
#def transaction(amount):
#    print('Received transaction signal with amount:', amount)
#    subprocess.run(['python3', '/home/maincharacter/mc/Text-toSpeech/trigger/ttl.py', str(amount)]) 
#    print("transaction")

@sio.event
def transaction(amount):
    print('Received transaction signal with amount:', amount)
    try:
        subprocess.run(['python', 'ttl.py', str(amount)], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing subprocess: {e}")
@sio.event
def disconnect():
    print('Disconnected from Node.js server')

if __name__ == "__main__":
    sio.connect('http://192.168.89.1:3000')  # Replace with your Node.js server IP
    sio.wait()
