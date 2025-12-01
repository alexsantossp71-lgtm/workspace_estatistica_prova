// ========================================
// ESTATÍSTICA APLICADA v2.0 - JAVASCRIPT
// ========================================

// ==================== THEME SYSTEM ====================
class ThemeManager {
    constructor() {
        this.theme = localStorage.getItem('theme') || 'dark';
        this.themeToggle = document.getElementById('theme-toggle');
        this.init();
    }

    init() {
        this.applyTheme(this.theme);
        if (this.themeToggle) {
            this.themeToggle.addEventListener('click', () => this.toggleTheme());
        }
    }

    applyTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        this.theme = theme;
        localStorage.setItem('theme', theme);

        // Update icon
        const icon = this.themeToggle.querySelector('.theme-icon');
        icon.textContent = theme === 'dark' ? '☀️' : '🌙';

        console.log(`🌓 Tema alterado para: ${theme}`);
    }

    toggleTheme() {
        const newTheme = this.theme === 'dark' ? 'light' : 'dark';
        this.applyTheme(newTheme);
    }
}

// ==================== SEARCH SYSTEM ====================
class SearchEngine {
    constructor() {
        this.searchInput = document.getElementById('search-input');
        this.searchResults = document.getElementById('search-results');
        this.chapters = this.buildIndex();
        this.init();
    }

    buildIndex() {
        return [
            {
                id: 1,
                title: 'Introdução à Estatística',
                keywords: ['população', 'amostra', 'dados', 'mensuração', 'amostragem'],
                url: 'chapter1.html',
                emoji: '🎯'
            },
            {
                id: 2,
                title: 'Estatística Descritiva',
                keywords: ['média', 'mediana', 'moda', 'variância', 'desvio', 'frequência'],
                url: 'chapter2.html',
                emoji: '📊'
            },
            {
                id: 3,
                title: 'Probabilidade',
                keywords: ['probabilidade', 'eventos', 'bayes', 'contagem', 'condicional'],
                url: 'chapter3.html',
                emoji: '🎲'
            },
            {
                id: 4,
                title: 'Distribuições Discretas',
                keywords: ['binomial', 'poisson', 'variável', 'aleatória', 'discreta'],
                url: 'chapter4.html',
                emoji: '📈'
            },
            {
                id: 5,
                title: 'Distribuição Normal',
                keywords: ['normal', 'gaussiana', 'sino', 'curva', 'padrão'],
                url: 'chapter5.html',
                emoji: '🔔'
            },
            {
                id: 6,
                title: 'Intervalos de Confiança',
                keywords: ['intervalo', 'confiança', 'estimação', 'parâmetro'],
                url: 'chapter6.html',
                emoji: '🎯'
            },
            {
                id: 7,
                title: 'Teste de Hipótese (1 Amostra)',
                keywords: ['hipótese', 'teste', 'significância', 'p-valor', 'amostra'],
                url: 'chapter7.html',
                emoji: '⚖️'
            },
            {
                id: 8,
                title: 'Teste de Hipótese (2 Amostras)',
                keywords: ['duas amostras', 'comparação', 'independente', 'dependente'],
                url: 'chapter8.html',
                emoji: '🔬'
            },
            {
                id: 9,
                title: 'Correlação e Regressão',
                keywords: ['correlação', 'regressão', 'linear', 'pearson', 'resíduos'],
                url: 'chapter9.html',
                emoji: '📉'
            },
            {
                id: 10,
                title: 'Qui-Quadrado e ANOVA',
                keywords: ['qui-quadrado', 'anova', 'variância', 'independência'],
                url: 'chapter10.html',
                emoji: 'χ²'
            }
        ];
    }

    init() {
        if (this.searchInput) {
            this.searchInput.addEventListener('input', (e) => this.handleSearch(e.target.value));

            document.addEventListener('click', (e) => {
                if (!this.searchInput.contains(e.target) && !this.searchResults.contains(e.target)) {
                    this.searchResults.classList.add('hidden');
                }
            });
        }
    }

    handleSearch(query) {
        if (!query || query.length < 2) {
            this.searchResults.classList.add('hidden');
            return;
        }

        const results = this.search(query);
        this.displayResults(results);
    }

    search(query) {
        const lowerQuery = query.toLowerCase();
        return this.chapters.filter(chapter => {
            const titleMatch = chapter.title.toLowerCase().includes(lowerQuery);
            const keywordMatch = chapter.keywords.some(k => k.toLowerCase().includes(lowerQuery));
            return titleMatch || keywordMatch;
        });
    }

    displayResults(results) {
        if (results.length === 0) {
            this.searchResults.innerHTML = '<div class="search-result-item">Nenhum resultado encontrado</div>';
            this.searchResults.classList.remove('hidden');
            return;
        }

        this.searchResults.innerHTML = results.map(r => `
            <a href="${r.url}" class="search-result-item">
                <div style="display: flex; align-items: center; gap: 1rem;">
                    <span style="font-size: 1.5rem;">${r.emoji}</span>
                    <div>
                        <div style="font-weight: 600; margin-bottom: 0.25rem;">Capítulo ${r.id}: ${r.title}</div>
                        <div style="font-size: 0.85rem; opacity: 0.7;">${r.keywords.slice(0, 3).join(', ')}</div>
                    </div>
                </div>
            </a>
        `).join('');

        this.searchResults.classList.remove('hidden');
    }
}

// ==================== PROGRESS TRACKER ====================
class ProgressTracker {
    constructor() {
        this.progress = this.loadProgress();
        this.progressBar = document.getElementById('progress-bar');
        this.progressPercentage = document.getElementById('progress-percentage');
        this.chaptersRead = document.getElementById('chapters-read');
        this.totalChapters = 10;
        this.init();
    }

    loadProgress() {
        const saved = localStorage.getItem('chapter-progress');
        return saved ? JSON.parse(saved) : {};
    }

    saveProgress() {
        localStorage.setItem('chapter-progress', JSON.stringify(this.progress));
    }

    init() {
        this.updateUI();
        this.markReadChapters();
    }

    markAsRead(chapterId) {
        this.progress[chapterId] = {
            read: true,
            timestamp: new Date().toISOString()
        };
        this.saveProgress();
        this.updateUI();
        this.markChapterCard(chapterId, true);

        console.log(`✅ Capítulo ${chapterId} marcado como lido!`);
    }

    markAsUnread(chapterId) {
        delete this.progress[chapterId];
        this.saveProgress();
        this.updateUI();
        this.markChapterCard(chapterId, false);

        console.log(`📋 Capítulo ${chapterId} marcado como não lido.`);
    }

    isRead(chapterId) {
        return !!this.progress[chapterId];
    }

    getProgress() {
        const read = Object.keys(this.progress).length;
        return Math.round((read / this.totalChapters) * 100);
    }

    updateUI() {
        const percentage = this.getProgress();
        const read = Object.keys(this.progress).length;

        this.progressBar.style.width = `${percentage}%`;
        this.progressPercentage.textContent = `${percentage}%`;
        this.chaptersRead.textContent = read;
    }

    markChapterCard(chapterId, isRead) {
        const card = document.querySelector(`.chapter-card[data-chapter="${chapterId}"]`);
        if (card) {
            if (isRead) {
                card.classList.add('read');
                const btn = card.querySelector('.mark-read-btn');
                if (btn) btn.textContent = '✓ Lido';
            } else {
                card.classList.remove('read');
                const btn = card.querySelector('.mark-read-btn');
                if (btn) btn.textContent = 'Marcar como lido';
            }
        }
    }

    markReadChapters() {
        Object.keys(this.progress).forEach(chapterId => {
            this.markChapterCard(chapterId, true);
        });
    }
}

// ==================== MAIN APP ====================
class App {
    constructor() {
        this.themeManager = new ThemeManager();
        this.searchEngine = new SearchEngine();
        this.progressTracker = new ProgressTracker();
        this.init();
    }

    init() {
        if (document.getElementById('start-btn')) {
            this.setupStartButton();
        }
        if (document.querySelector('.chapter-card')) {
            this.setupChapterCards();
        }
        this.logWelcome();
    }

    setupStartButton() {
        const startBtn = document.getElementById('start-btn');
        const contentSection = document.getElementById('content-section');

        startBtn.addEventListener('click', () => {
            contentSection.classList.remove('hidden');
            setTimeout(() => {
                contentSection.classList.add('visible');
                contentSection.scrollIntoView({ behavior: 'smooth' });
            }, 10);
        });
    }

    setupChapterCards() {
        // Mark read buttons are handled by global function
        // to avoid event propagation issues with links
    }

    logWelcome() {
        console.log('%c📊 Estatística Aplicada v2.0 BETA', 'color: #4f46e5; font-size: 24px; font-weight: bold;');
        console.log('%c🚀 Novidades:', 'color: #ec4899; font-size: 16px; font-weight: bold;');
        console.log('%c  🔍 Sistema de Busca', 'color: #14b8a6; font-size: 14px;');
        console.log('%c  🌓 Modo Escuro/Claro', 'color: #14b8a6; font-size: 14px;');
        console.log('%c  📈 Rastreamento de Progresso', 'color: #14b8a6; font-size: 14px;');
        console.log('%c  ⚡ Interface Melhorada', 'color: #14b8a6; font-size: 14px;');
        console.log('%c\n💡 Dica: Use o botão de tema no topo para alternar entre claro/escuro!', 'color: #94a3b8; font-size: 12px;');
    }
}

// ==================== GLOBAL FUNCTIONS ====================
function toggleRead(event, chapterId) {
    event.preventDefault();
    event.stopPropagation();

    const tracker = window.app.progressTracker;

    if (tracker.isRead(chapterId)) {
        tracker.markAsUnread(chapterId);
    } else {
        tracker.markAsRead(chapterId);
    }
}

// ==================== INITIALIZE ====================
document.addEventListener('DOMContentLoaded', () => {
    window.app = new App();
});
