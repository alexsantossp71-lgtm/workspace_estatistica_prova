// Theme Loader for Chapter Pages
(function () {
    // 1. Get theme from localStorage or default to dark
    const savedTheme = localStorage.getItem('theme') || 'dark';

    // 2. Apply theme immediately to prevent flash
    document.documentElement.setAttribute('data-theme', savedTheme);

    // 3. Setup toggle button when DOM is ready
    document.addEventListener('DOMContentLoaded', () => {
        const toggleBtn = document.getElementById('theme-toggle-chapter');
        if (toggleBtn) {
            // Set initial icon
            updateIcon(toggleBtn, savedTheme);

            toggleBtn.addEventListener('click', () => {
                const currentTheme = document.documentElement.getAttribute('data-theme');
                const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

                document.documentElement.setAttribute('data-theme', newTheme);
                localStorage.setItem('theme', newTheme);
                updateIcon(toggleBtn, newTheme);
            });
        }
    });

    function updateIcon(btn, theme) {
        const iconSpan = btn.querySelector('.theme-icon');
        if (iconSpan) {
            iconSpan.textContent = theme === 'dark' ? '☀️' : '🌙';
        }
    }
})();
