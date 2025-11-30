# 🚀 Quick Start - Versão 2.0

## 🎯 Primeiras Tarefas para Iniciar a v2.0

Este guia contém as primeiras ações práticas para começar o desenvolvimento da versão 2.0.

---

## ✅ Pré-requisitos

Antes de começar, certifique-se de que a v1.0 está completa:
- [x] index.html com footer de versão
- [x] Capítulos 1 e 2 completos
- [x] Documentação criada (README, CHANGELOG, etc.)
- [x] version.json configurado

---

## 🎨 TAREFA 1: Implementar Modo Escuro (Quick Win!)

### Prioridade: ALTA | Complexidade: BAIXA | Tempo: 1-2 dias

### Passo 1: Criar Paleta de Cores para Modo Escuro

Adicione ao `css/style.css`:

```css
/* Adicionar no início do arquivo, após as variáveis existentes */

/* Tema Claro (padrão - já existe) */
:root {
  /* Cores já existentes... */
  --primary-color: hsl(243, 75%, 59%);
  --secondary-color: hsl(330, 81%, 60%);
  --accent-color: hsl(168, 76%, 42%);
  
  /* Adicionar variáveis de tema */
  --bg-primary: hsl(0, 0%, 98%);
  --bg-secondary: hsl(0, 0%, 95%);
  --text-primary: hsl(240, 21%, 15%);
  --text-secondary: hsl(0, 0%, 30%);
  --border-color: rgba(0, 0, 0, 0.1);
}

/* Tema Escuro */
[data-theme="dark"] {
  --bg-primary: hsl(240, 21%, 10%);
  --bg-secondary: hsl(240, 21%, 15%);
  --text-primary: hsl(0, 0%, 95%);
  --text-secondary: hsl(0, 0%, 70%);
  --border-color: rgba(255, 255, 255, 0.1);
  --glass-bg: rgba(255, 255, 255, 0.05);
  --glass-border: rgba(255, 255, 255, 0.1);
}

/* Transição suave entre temas */
* {
  transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease;
}
```

### Passo 2: Criar Toggle de Tema

Adicione ao `index.html` (no header, antes do título):

```html
<!-- Adicionar no header -->
<div class="theme-toggle-container">
  <button id="theme-toggle" class="theme-toggle" aria-label="Alternar tema">
    <span class="sun-icon">☀️</span>
    <span class="moon-icon">🌙</span>
  </button>
</div>
```

### Passo 3: Adicionar JavaScript para Toggle

Adicione ao final do `index.html` (antes do fechamento do `</script>`):

```javascript
// Sistema de Tema
const themeToggle = document.getElementById('theme-toggle');
const htmlElement = document.documentElement;

// Carregar tema salvo
const savedTheme = localStorage.getItem('theme') || 'light';
htmlElement.setAttribute('data-theme', savedTheme);

// Toggle de tema
themeToggle.addEventListener('click', () => {
  const currentTheme = htmlElement.getAttribute('data-theme');
  const newTheme = currentTheme === 'light' ? 'dark' : 'light';
  
  htmlElement.setAttribute('data-theme', newTheme);
  localStorage.setItem('theme', newTheme);
  
  console.log(`🌓 Tema alterado para: ${newTheme}`);
});
```

### Passo 4: Estilizar o Toggle

Adicione ao `css/style.css`:

```css
.theme-toggle-container {
  position: fixed;
  top: 2rem;
  right: 2rem;
  z-index: 1000;
}

.theme-toggle {
  background: var(--glass-bg);
  border: 1px solid var(--glass-border);
  border-radius: 50px;
  padding: 0.8rem 1.2rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  backdrop-filter: blur(10px);
  transition: all 0.3s ease;
}

.theme-toggle:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

[data-theme="light"] .moon-icon {
  display: none;
}

[data-theme="dark"] .sun-icon {
  display: none;
}
```

### ✅ Checklist Modo Escuro
- [ ] Adicionar variáveis CSS para tema escuro
- [ ] Criar botão de toggle no header
- [ ] Implementar JavaScript de alternância
- [ ] Salvar preferência em LocalStorage
- [ ] Estilizar o botão de toggle
- [ ] Testar em todas as páginas
- [ ] Aplicar em todos os capítulos

---

## 🔍 TAREFA 2: Sistema de Busca Básico

### Prioridade: ALTA | Complexidade: MÉDIA | Tempo: 3-4 dias

### Passo 1: Criar Interface de Busca

Adicione ao `index.html` (após o header):

```html
<div class="search-container">
  <div class="search-box">
    <input 
      type="text" 
      id="search-input" 
      placeholder="🔍 Buscar em todos os capítulos..."
      autocomplete="off"
    />
    <div id="search-results" class="search-results hidden"></div>
  </div>
</div>
```

### Passo 2: Criar Índice de Busca

Crie arquivo `js/search-index.json`:

```json
{
  "chapters": [
    {
      "id": 1,
      "title": "Introdução à Estatística",
      "keywords": ["população", "amostra", "dados", "mensuração"],
      "url": "chapter1.html"
    },
    {
      "id": 2,
      "title": "Estatística Descritiva",
      "keywords": ["média", "mediana", "moda", "variância"],
      "url": "chapter2.html"
    }
  ]
}
```

### Passo 3: Implementar Busca (JavaScript)

Crie arquivo `js/search.js`:

```javascript
class SearchEngine {
  constructor() {
    this.index = [];
    this.loadIndex();
  }

  async loadIndex() {
    const response = await fetch('js/search-index.json');
    const data = await response.json();
    this.index = data.chapters;
  }

  search(query) {
    if (!query || query.length < 2) return [];
    
    const lowerQuery = query.toLowerCase();
    return this.index.filter(chapter => {
      const titleMatch = chapter.title.toLowerCase().includes(lowerQuery);
      const keywordMatch = chapter.keywords.some(k => 
        k.toLowerCase().includes(lowerQuery)
      );
      return titleMatch || keywordMatch;
    });
  }
}

// Inicializar busca
const searchEngine = new SearchEngine();
const searchInput = document.getElementById('search-input');
const searchResults = document.getElementById('search-results');

searchInput.addEventListener('input', (e) => {
  const query = e.target.value;
  const results = searchEngine.search(query);
  
  if (results.length > 0) {
    searchResults.innerHTML = results.map(r => `
      <a href="${r.url}" class="search-result-item">
        <strong>${r.title}</strong>
        <span>${r.keywords.join(', ')}</span>
      </a>
    `).join('');
    searchResults.classList.remove('hidden');
  } else {
    searchResults.classList.add('hidden');
  }
});
```

### ✅ Checklist Busca
- [ ] Criar interface de busca
- [ ] Criar índice de busca (JSON)
- [ ] Implementar lógica de busca
- [ ] Estilizar resultados
- [ ] Adicionar destaque de termos
- [ ] Testar com diferentes queries

---

## 📈 TAREFA 3: Rastreamento de Progresso

### Prioridade: ALTA | Complexidade: MÉDIA | Tempo: 2-3 dias

### Passo 1: Criar Sistema de Progresso

Crie arquivo `js/progress.js`:

```javascript
class ProgressTracker {
  constructor() {
    this.progress = this.loadProgress();
  }

  loadProgress() {
    const saved = localStorage.getItem('chapter-progress');
    return saved ? JSON.parse(saved) : {};
  }

  saveProgress() {
    localStorage.setItem('chapter-progress', JSON.stringify(this.progress));
  }

  markAsRead(chapterId) {
    this.progress[chapterId] = {
      read: true,
      timestamp: new Date().toISOString()
    };
    this.saveProgress();
    this.updateUI();
  }

  getProgress() {
    const total = 10;
    const read = Object.keys(this.progress).length;
    return Math.round((read / total) * 100);
  }

  updateUI() {
    const percentage = this.getProgress();
    const progressBar = document.getElementById('progress-bar');
    if (progressBar) {
      progressBar.style.width = `${percentage}%`;
      progressBar.textContent = `${percentage}% completo`;
    }
  }
}

// Inicializar
const progressTracker = new ProgressTracker();
progressTracker.updateUI();
```

### Passo 2: Adicionar Barra de Progresso

Adicione ao `index.html` (antes do chapters-grid):

```html
<div class="progress-section">
  <h3>📊 Seu Progresso</h3>
  <div class="progress-bar-container">
    <div id="progress-bar" class="progress-bar">0% completo</div>
  </div>
  <p class="progress-stats">
    <span id="chapters-read">0</span> de 10 capítulos lidos
  </p>
</div>
```

### ✅ Checklist Progresso
- [ ] Criar classe ProgressTracker
- [ ] Implementar salvamento em LocalStorage
- [ ] Adicionar barra de progresso visual
- [ ] Marcar capítulos como lidos
- [ ] Mostrar estatísticas
- [ ] Adicionar badges de conquistas

---

## 📝 TAREFA 4: Quiz Básico (Capítulo 1)

### Prioridade: ALTA | Complexidade: ALTA | Tempo: 4-5 dias

### Passo 1: Criar Estrutura de Quiz

Crie arquivo `js/quiz-data.json`:

```json
{
  "chapter1": {
    "title": "Quiz - Introdução à Estatística",
    "questions": [
      {
        "id": 1,
        "question": "O que é uma população em estatística?",
        "options": [
          "Conjunto de todos os elementos de interesse",
          "Subconjunto da amostra",
          "Apenas pessoas",
          "Dados coletados"
        ],
        "correct": 0,
        "explanation": "População é o conjunto completo de todos os elementos que queremos estudar."
      },
      {
        "id": 2,
        "question": "Qual é a diferença entre dados qualitativos e quantitativos?",
        "options": [
          "Não há diferença",
          "Qualitativos são categorias, quantitativos são números",
          "Qualitativos são números, quantitativos são categorias",
          "Ambos são iguais"
        ],
        "correct": 1,
        "explanation": "Dados qualitativos descrevem características (categorias), enquanto quantitativos são numéricos."
      }
    ]
  }
}
```

### Passo 2: Implementar Quiz Engine

Crie arquivo `js/quiz.js`:

```javascript
class QuizEngine {
  constructor(chapterId) {
    this.chapterId = chapterId;
    this.questions = [];
    this.currentQuestion = 0;
    this.score = 0;
    this.loadQuestions();
  }

  async loadQuestions() {
    const response = await fetch('js/quiz-data.json');
    const data = await response.json();
    this.questions = data[this.chapterId].questions;
    this.renderQuestion();
  }

  renderQuestion() {
    const q = this.questions[this.currentQuestion];
    const container = document.getElementById('quiz-container');
    
    container.innerHTML = `
      <div class="quiz-question">
        <h3>Questão ${this.currentQuestion + 1} de ${this.questions.length}</h3>
        <p class="question-text">${q.question}</p>
        <div class="options">
          ${q.options.map((opt, i) => `
            <button class="option-btn" data-index="${i}">
              ${opt}
            </button>
          `).join('')}
        </div>
      </div>
    `;

    // Adicionar event listeners
    document.querySelectorAll('.option-btn').forEach(btn => {
      btn.addEventListener('click', (e) => this.checkAnswer(e));
    });
  }

  checkAnswer(e) {
    const selected = parseInt(e.target.dataset.index);
    const q = this.questions[this.currentQuestion];
    
    if (selected === q.correct) {
      this.score++;
      this.showFeedback(true, q.explanation);
    } else {
      this.showFeedback(false, q.explanation);
    }
  }

  showFeedback(correct, explanation) {
    // Implementar feedback visual
    alert(correct ? '✅ Correto!' : '❌ Incorreto');
    alert(`💡 ${explanation}`);
    
    this.currentQuestion++;
    if (this.currentQuestion < this.questions.length) {
      this.renderQuestion();
    } else {
      this.showResults();
    }
  }

  showResults() {
    const percentage = (this.score / this.questions.length) * 100;
    alert(`🎉 Quiz completo! Você acertou ${this.score} de ${this.questions.length} (${percentage}%)`);
  }
}
```

### ✅ Checklist Quiz
- [ ] Criar estrutura de dados de questões
- [ ] Implementar QuizEngine
- [ ] Criar interface visual do quiz
- [ ] Adicionar feedback imediato
- [ ] Implementar sistema de pontuação
- [ ] Criar tela de resultados
- [ ] Adicionar explicações detalhadas

---

## 🎯 Ordem de Implementação Sugerida

### Semana 1
1. ✅ **Modo Escuro** (1-2 dias) - Quick win!
2. ✅ **Melhorar Navegação** (1 dia) - Botões anterior/próximo

### Semana 2
3. ✅ **Rastreamento de Progresso** (2-3 dias)
4. ✅ **Sistema de Favoritos Básico** (2 dias)

### Semana 3-4
5. ✅ **Sistema de Busca** (3-4 dias)
6. ✅ **Quiz Básico** (4-5 dias)

---

## 📊 Checklist Geral de Início

### Setup
- [ ] Criar branch `develop` no Git
- [ ] Atualizar version.json para "2.0.0-dev"
- [ ] Criar pasta `features/` para organização

### Quick Wins (Começar aqui!)
- [ ] Implementar modo escuro
- [ ] Adicionar botões de navegação entre capítulos
- [ ] Criar sistema de favoritos básico

### Features Principais
- [ ] Sistema de busca global
- [ ] Rastreamento de progresso
- [ ] Quiz interativo
- [ ] Calculadora estatística

### Conteúdo
- [ ] Completar capítulo 3
- [ ] Completar capítulo 4
- [ ] Completar capítulo 6
- [ ] Completar capítulo 7
- [ ] Completar capítulo 8

---

## 🚀 Como Começar AGORA

### Opção 1: Modo Escuro (Mais Fácil)
```bash
1. Abrir css/style.css
2. Adicionar variáveis de tema escuro
3. Abrir index.html
4. Adicionar botão de toggle
5. Adicionar JavaScript de alternância
6. Testar!
```

### Opção 2: Busca (Mais Impacto)
```bash
1. Criar js/search-index.json
2. Criar js/search.js
3. Adicionar interface de busca no index.html
4. Estilizar resultados
5. Testar buscas
```

---

## 📝 Notas Importantes

- **Sempre testar** em múltiplos navegadores
- **Commitar frequentemente** com mensagens claras
- **Documentar** mudanças no CHANGELOG.md
- **Manter** compatibilidade com v1.0

---

<div align="center">

### 🎯 Pronto para começar a v2.0! 🚀

**Escolha uma tarefa e mãos à obra!**

</div>

---

**Data:** 30 de Novembro de 2025  
**Versão Alvo:** 2.0.0  
**Status:** Pronto para desenvolvimento
