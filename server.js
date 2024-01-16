const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const cors = require('cors');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

app.use(cors());
app.use(express.static('public'));
app.use(express.json()); // Add this line to parse JSON in the request body

io.on('connection', (socket) => {
    console.log('Client connected');

    socket.on('transaction', (amount) => {
        console.log('Transaction occurred with amount:', amount);
        io.emit('transaction', amount);
    });
});

app.post('/transaction', (req, res) => {
    const amount = req.body.amount;
    console.log('Received POST request to /transaction with amount:', amount);
    // Handle the transaction as needed
    res.status(200).json({ message: 'Transaction processed successfully' });
});

const PORT = process.env.PORT || 3000;

server.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}`);
});
