// ============================================
// ARCHIVO: static/js/main.js
// AUTOR: Gustavo Vallejo
// FECHA: 06 de Abril de 2026
// ============================================

document.addEventListener('DOMContentLoaded', function () {
    iniciarModoOscuro();
    iniciarBuscador();
    console.log('🐍 AtriumEdu: Funcionalidades extra cargadas');
});

/**
 * 1. Lógica del Modo Oscuro
 */
function iniciarModoOscuro() {
    const toggleBtn = document.getElementById('theme-toggle');
    const body = document.body;

    // Verificar preferencia guardada
    const savedTheme = localStorage.getItem('atriumedu-theme');
    if (savedTheme === 'dark') {
        body.classList.add('dark-mode');
        if (toggleBtn) toggleBtn.innerHTML = '☀️ Claro';
    } else {
        if (toggleBtn) toggleBtn.innerHTML = '🌙 Oscuro';
    }

    if (toggleBtn) {
        toggleBtn.addEventListener('click', () => {
            body.classList.toggle('dark-mode');
            const isDark = body.classList.contains('dark-mode');

            // Guardar preferencia
            localStorage.setItem('atriumedu-theme', isDark ? 'dark' : 'light');

            // Actualizar texto del botón
            toggleBtn.innerHTML = isDark ? '☀️ Claro' : '🌙 Oscuro';
        });
    }
}

/**
 * 2. Lógica del Buscador
 */
function iniciarBuscador() {
    const searchInput = document.getElementById('search-input');
    const cards = document.querySelectorAll('.card');

    if (!searchInput) return;

    searchInput.addEventListener('keyup', (e) => {
        const term = e.target.value.toLowerCase();

        cards.forEach(card => {
            const title = card.querySelector('h3').textContent.toLowerCase();
            const desc = card.querySelector('p').textContent.toLowerCase();

            if (title.includes(term) || desc.includes(term)) {
                card.style.display = 'block';
                // Efecto de resaltado sutil
                card.style.opacity = '1';
                card.style.transform = 'scale(1)';
            } else {
                card.style.display = 'none';
                card.style.opacity = '0';
                card.style.transform = 'scale(0.95)';
            }
        });
    });
}

// ==================== CONTADOR DE PROGRESO ====================

function initProgreso() {
    const TOTAL_CLASES = 11;
    const progresoKey = 'atriumedu-progreso';

    // Obtener clases completadas
    let completadas = JSON.parse(localStorage.getItem(progresoKey)) || [];

    // Actualizar UI
    actualizarBarraProgreso(completadas.length, TOTAL_CLASES);

    // Marcar clases completadas al visitar
    document.addEventListener('DOMContentLoaded', () => {
        const currentPage = window.location.pathname.split('/').pop();
        if (currentPage && currentPage.endsWith('.html') && currentPage !== 'index.html') {
            marcarComoCompletada(currentPage, completadas);
        }
    });

    // Botón resetear
    const resetBtn = document.getElementById('reset-progreso');
    if (resetBtn) {
        resetBtn.addEventListener('click', () => {
            if (confirm('¿Estás seguro de reiniciar tu progreso?')) {
                localStorage.removeItem(progresoKey);
                location.reload();
            }
        });
    }
}

function actualizarBarraProgreso(completadas, total) {
    const porcentaje = Math.round((completadas / total) * 100);
    const texto = document.getElementById('progreso-texto');
    const barra = document.getElementById('barra-progreso');

    if (texto) texto.textContent = `${completadas} de $${total} ($${porcentaje}%)`;
    if (barra) barra.style.width = `${porcentaje}%`;

    // Celebrar al completar 100%
    if (porcentaje === 100) {
        lanzarConfeti();
    }
}

function marcarComoCompletada(page, completadas) {
    if (!completadas.includes(page)) {
        completadas.push(page);
        localStorage.setItem('atriumedu-progreso', JSON.stringify(completadas));
        actualizarBarraProgreso(completadas.length, 11);
    }
}

// Llamar al inicio
document.addEventListener('DOMContentLoaded', initProgreso);

// ==================== EFECTO CONFETI ====================

function lanzarConfeti() {
    const duration = 3000;
    const end = Date.now() + duration;

    (function frame() {
        confetti({
            particleCount: 5,
            angle: 60,
            spread: 55,
            origin: { x: 0 },
            colors: ['#4A90E2', '#50E3C2', '#F5A623', '#7ED321', '#BD10E0']
        });
        confetti({
            particleCount: 5,
            angle: 120,
            spread: 55,
            origin: { x: 1 },
            colors: ['#4A90E2', '#50E3C2', '#F5A623', '#7ED321', '#BD10E0']
        });

        if (Date.now() < end) {
            requestAnimationFrame(frame);
        }
    }());
}

// Celebrar al completar curso
function celebrarCurso() {
    confetti({
        particleCount: 150,
        spread: 70,
        origin: { y: 0.6 },
        colors: ['#4A90E2', '#50E3C2', '#F5A623', '#7ED321', '#BD10E0']
    });

    // Mensaje de felicitación
    setTimeout(() => {
        alert('🎉 ¡FELICIDADES! Has completado todo el curso de Python 🐍');
    }, 500);
}

// ==================== CONTADOR DE PROGRESO ====================

function initProgreso() {
    const TOTAL_CLASES = 11;
    const progresoKey = 'atriumedu-progreso';

    // Obtener clases completadas
    let completadas = JSON.parse(localStorage.getItem(progresoKey)) || [];

    // Actualizar UI
    actualizarBarraProgreso(completadas.length, TOTAL_CLASES);

    // Marcar clases completadas al visitar
    document.addEventListener('DOMContentLoaded', () => {
        const currentPage = window.location.pathname.split('/').pop();
        if (currentPage && currentPage.endsWith('.html') && currentPage !== 'index.html') {
            marcarComoCompletada(currentPage, completadas);
        }
    });

    // Botón resetear
    const resetBtn = document.getElementById('reset-progreso');
    if (resetBtn) {
        resetBtn.addEventListener('click', () => {
            if (confirm('¿Estás seguro de reiniciar tu progreso?')) {
                localStorage.removeItem(progresoKey);
                location.reload();
            }
        });
    }
}

function actualizarBarraProgreso(completadas, total) {
    const porcentaje = Math.round((completadas / total) * 100);
    const texto = document.getElementById('progreso-texto');
    const barra = document.getElementById('barra-progreso');

    if (texto) texto.textContent = `${completadas} de $${total} ($${porcentaje}%)`;
    if (barra) barra.style.width = `${porcentaje}%`;

    // Celebrar al completar 100%
    if (porcentaje === 100) {
        lanzarConfeti();
    }
}

function marcarComoCompletada(page, completadas) {
    if (!completadas.includes(page)) {
        completadas.push(page);
        localStorage.setItem(progresoKey, JSON.stringify(completadas));
        actualizarBarraProgreso(completadas.length, 11);
    }
}

// Llamar al inicio
document.addEventListener('DOMContentLoaded', initProgreso);