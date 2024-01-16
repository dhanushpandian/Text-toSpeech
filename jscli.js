
const io = require('socket.io-client');
const { exec } = require('child_process');
console.log("Started client...");


const socket = io('http://192.168.89.1:3000') ;



// Socket.io event handlers
socket.on('connect', () => {
    console.log('Connected to Node.js server');
});

socket.on('transaction', (amount) => {
    console.log('Received transaction signal with amount:', amount);
    try {
        // Execute the text-to-speech script using child_process
        console.log('Calling text-to-speech subprocess...');
        exec(`python3 /home/maincharacter/mc/Text-toSpeech/trigger/ttl.py ${amount}`, (error, stdout, stderr) => {
            if (error) {
                console.error(`Error calling text-to-speech subprocess: ${error.message}`);
            } else {
                console.log('Text-to-speech subprocess completed successfully:', stdout);
            }
        });
    } catch (error) {
        console.error('Error calling text-to-speech subprocess:', error.message);
    }
});

socket.on('disconnect', () => {
    console.log('Disconnected from Node.js server');
});

// Connect to the Node.js server
socket.connect();