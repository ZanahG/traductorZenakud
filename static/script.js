function translateText() {
    const text = document.getElementById('inputText').value;
    document.getElementById('inputText').value = ''; 
    if (text.trim() === '') {
        return; 
    }
    fetch('/traducir', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ texto: text })
    })
    .then(response => response.json())
    .then(data => {
        const messageContainer = document.createElement('div');
        messageContainer.className = 'message';

        const icon = document.createElement('img');
        icon.src = '/static/mod_icon.png';
        icon.className = 'icon';

        const messageText = document.createElement('span');
        messageText.textContent = `Zenakud: ${data.traduccion}`;

        messageContainer.appendChild(icon);
        messageContainer.appendChild(messageText);
        document.getElementById('messages').prepend(messageContainer); // Agregar el mensaje al principio
    })
    .catch(error => console.error('Error:', error));
}