// ============================================
// ARCHIVO: static/js/nav.js
// AUTOR: Gustavo Vallejo
// FECHA: 06 de Abril de 2026
// ============================================

document.addEventListener('DOMContentLoaded', function () {
    initSmartDropdown();
});

function initSmartDropdown() {
    const dropdown = document.querySelector('.dropdown');
    const content = document.querySelector('.dropdown-content');

    if (!dropdown || !content) return;

    let timeout; // Temporizador para evitar parpadeo

    // Función para abrir
    const openDropdown = () => {
        clearTimeout(timeout);
        content.classList.add('show');
    };

    // Función para cerrar (con delay)
    const closeDropdown = () => {
        timeout = setTimeout(() => {
            content.classList.remove('show');
        }, 150); // 150ms de espera antes de cerrar
    };

    // Eventos en el botón (dropdown)
    dropdown.addEventListener('mouseenter', openDropdown);
    dropdown.addEventListener('mouseleave', closeDropdown);

    // Eventos en el contenido del dropdown
    content.addEventListener('mouseenter', () => {
        clearTimeout(timeout); // Si entro al dropdown, no cerrar
    });
    content.addEventListener('mouseleave', closeDropdown);

    // Cerrar al hacer click fuera
    document.addEventListener('click', (e) => {
        if (!dropdown.contains(e.target)) {
            content.classList.remove('show');
        }
    });
}