async function traducir() {
    let texto = document.getElementById('inputText').value;
    let response = await fetch('https://traductorzenakud-production.up.railway.app', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({texto: texto})
    });
    if (response.ok) {
        let data = await response.json();
        document.getElementById('resultado').innerText = data.traduccion;
    } else {
        document.getElementById('resultado').innerText = 'Error en la traducción. Inténtalo de nuevo.';
    }
}
