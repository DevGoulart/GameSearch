const checkbox = document.getElementById('checkbox');
const body = document.body;

checkbox.addEventListener('change', () => {
    body.classList.toggle('dark-mode');
    const isDarkMode = body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDarkMode);
});

// Carregar preferência do usuário
if (localStorage.getItem('darkMode') === 'true') {
    body.classList.add('dark-mode');
    checkbox.checked = true;
} else {
    body.classList.remove('dark-mode');
    checkbox.checked = false;
}