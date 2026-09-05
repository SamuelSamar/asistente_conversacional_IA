function mostrarRecordatorio(mensaje) {
    const zona = document.getElementById('zona-recordatorio');
    const texto = document.getElementById('mensaje-recordatorio');
    texto.textContent = mensaje;
    zona.classList.remove('hidden');
    hablar(mensaje, 3);
}

function revisarMedicamentos() {
    const ahora = new Date();
    const horaActual = ahora.toTimeString().slice(0, 5);

    medicamentos.forEach(med => {
        if (med.hora === horaActual) {
            const mensaje = `Es hora de tomar ${med.medicamento}, dosis: ${med.dosis}`;
            mostrarRecordatorio(mensaje);
        }
    });
}

setInterval(revisarMedicamentos, 60000);