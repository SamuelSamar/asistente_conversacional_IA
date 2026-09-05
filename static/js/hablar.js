function hablar(texto, repeticiones = 1) {
    let contador = 0;
    const repetir = () => {
        if (contador < repeticiones) {
            const speech = new SpeechSynthesisUtterance();
            speech.lang = 'es-PE';
            speech.text = texto;
            speech.rate = 0.95;
            speech.pitch = 1;
            speechSynthesis.speak(speech);
            contador++;
            setTimeout(repetir, 3000);
        }
    };
    repetir();
}