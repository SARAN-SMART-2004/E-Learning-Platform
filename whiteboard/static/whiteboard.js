// static/whiteboard.js

const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
let drawing = false;

const ws = new WebSocket('ws://' + window.location.host + '/ws/whiteboard/');

ws.onmessage = function(e) {
    const data = JSON.parse(e.data);
    drawOnCanvas(data.x, data.y);
};

canvas.addEventListener('mousedown', () => drawing = true);
canvas.addEventListener('mouseup', () => drawing = false);

canvas.addEventListener('mousemove', (event) => {
    if (!drawing) return;
    const x = event.offsetX;
    const y = event.offsetY;
    drawOnCanvas(x, y);
    ws.send(JSON.stringify({x: x, y: y}));
});

function drawOnCanvas(x, y) {
    ctx.fillStyle = 'black';
    ctx.fillRect(x, y, 2, 2);
}
