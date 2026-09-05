const btnMicrofono = document.getElementById('btnMicrofono');
const campoMensaje = document.querySelector('input[name="mensaje"]');
let reconocimiento;
if ('webkitSpeechRecognition' in window) {
    reconocimiento = new webkitSpeechRecognition();
    reconocimiento.lang = 'es-PE';
    reconocimiento.continuous = false;
    reconocimiento.interimResults = false;

    btnMicrofono.addEventListener('click', function () {
        reconocimiento.start();
        btnMicrofono.classList.add('bg-blue-200');
    });

    reconocimiento.onresult = function (event) {
        const resultado = event.results[0][0].transcript;
        campoMensaje.value = resultado;
        campoMensaje.form.requestSubmit();
        btnMicrofono.classList.remove('bg-blue-200');
    };

    reconocimiento.onerror = function () {
        btnMicrofono.classList.remove('bg-blue-200');
    };

    reconocimiento.onend = function () {
        btnMicrofono.classList.remove('bg-blue-200');
    };
} else {
    btnMicrofono.disabled = true;
    btnMicrofono.title = "Tu navegador no soporta reconocimiento de voz";
}