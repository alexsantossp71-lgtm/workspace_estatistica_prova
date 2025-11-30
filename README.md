# 📊 Estatística Aplicada - Website Interativo

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

> **Plataforma educacional interativa** baseada no livro "Estatística Aplicada" de Larson & Farber (6ª Edição)

## 🎯 Visão Geral

Este projeto transforma o conteúdo do livro de Estatística Aplicada em uma experiência web moderna, interativa e visualmente atraente. Desenvolvido com foco em UX/UI premium e didática eficiente.

## ✨ Características

### 🎨 Design Moderno
- **Glassmorphism** - Efeitos de vidro fosco e transparências
- **Gradientes Vibrantes** - Paleta de cores HSL cuidadosamente selecionada
- **Animações Suaves** - Transições e micro-interações
- **Responsivo** - Funciona perfeitamente em desktop, tablet e mobile
- **Tipografia Premium** - Google Fonts (Outfit)

### 📚 Conteúdo Educacional
- **10 Capítulos Completos** cobrindo todo o programa
- **Explicações Detalhadas** de todos os conceitos
- **Exemplos Práticos** do mundo real
- **Exercícios Resolvidos** passo a passo
- **Visualizações Interativas** com Chart.js
- **SVGs Didáticos** para conceitos complexos

### 🚀 Funcionalidades (v1.0)
- ✅ Navegação intuitiva por capítulos
- ✅ Hero section animada
- ✅ Cards interativos com hover effects
- ✅ Gráficos dinâmicos (Chart.js)
- ✅ Layout responsivo
- ✅ Performance otimizada

## 📁 Estrutura do Projeto

```
workspace_estatistica_prova/
│
├── 📄 index.html              # Página principal
├── 📄 chapter1.html           # Capítulo 1: Introdução à Estatística ✅
├── 📄 chapter2.html           # Capítulo 2: Estatística Descritiva ✅
├── 📄 chapter3.html           # Capítulo 3: Probabilidade
├── 📄 chapter4.html           # Capítulo 4: Distribuições Discretas
├── 📄 chapter5.html           # Capítulo 5: Distribuição Normal
├── 📄 chapter6.html           # Capítulo 6: Intervalos de Confiança
├── 📄 chapter7.html           # Capítulo 7: Teste de Hipótese (1 Amostra)
├── 📄 chapter8.html           # Capítulo 8: Teste de Hipótese (2 Amostras)
├── 📄 chapter9.html           # Capítulo 9: Correlação e Regressão
├── 📄 chapter10.html          # Capítulo 10: Qui-Quadrado e ANOVA
│
├── 📁 css/
│   └── style.css              # Estilos globais
│
├── 📁 js/
│   └── main.js                # Scripts principais
│
├── 📁 images/                 # Imagens e SVGs
│
├── 📁 scripts/                # Scripts Python auxiliares
│   ├── generate_chapters.py
│   ├── add_visualizations.py
│   └── review_charts.py
│
├── 📁 src/                    # Arquivos fonte
│
├── 📄 CHANGELOG.md            # Histórico de versões
├── 📄 README.md               # Este arquivo
└── 📄 package.json            # Dependências (se houver)
```

## 🚀 Como Usar

### Opção 1: Abrir Diretamente
1. Clone ou baixe este repositório
2. Abra o arquivo `index.html` em seu navegador
3. Clique em "Começar a Estudar"
4. Navegue pelos capítulos

### Opção 2: Servidor Local (Recomendado)
```bash
# Com Python
python -m http.server 8000

# Com Node.js (http-server)
npx http-server

# Com PHP
php -S localhost:8000
```

Depois acesse: `http://localhost:8000`

## 📊 Status dos Capítulos

| Capítulo | Título | Status | Conteúdo |
|----------|--------|--------|----------|
| 1 | Introdução à Estatística | ✅ Completo | 100% |
| 2 | Estatística Descritiva | ✅ Completo | 100% |
| 3 | Probabilidade | 📋 Estrutura | 30% |
| 4 | Distribuições Discretas | 📋 Estrutura | 20% |
| 5 | Distribuição Normal | 📋 Estrutura | 40% |
| 6 | Intervalos de Confiança | 📋 Estrutura | 20% |
| 7 | Teste de Hipótese (1 Amostra) | 📋 Estrutura | 30% |
| 8 | Teste de Hipótese (2 Amostras) | 📋 Estrutura | 30% |
| 9 | Correlação e Regressão | 📋 Estrutura | 40% |
| 10 | Qui-Quadrado e ANOVA | 📋 Estrutura | 40% |

## 🛠️ Tecnologias Utilizadas

### Frontend
- **HTML5** - Estrutura semântica
- **CSS3** - Estilos modernos com variáveis CSS
- **JavaScript (Vanilla)** - Interatividade
- **Chart.js** - Gráficos interativos
- **Google Fonts** - Tipografia (Outfit)

### Ferramentas de Desenvolvimento
- **Python** - Scripts de geração de conteúdo
- **Git** - Controle de versão
- **VS Code** - Editor recomendado

## 🎨 Paleta de Cores

```css
--primary-color: hsl(243, 75%, 59%)      /* Roxo vibrante */
--secondary-color: hsl(330, 81%, 60%)    /* Rosa vibrante */
--accent-color: hsl(168, 76%, 42%)       /* Verde-água */
--bg-dark: hsl(240, 21%, 15%)            /* Fundo escuro */
--text-light: hsl(0, 0%, 95%)            /* Texto claro */
--text-muted: hsl(0, 0%, 70%)            /* Texto secundário */
```

## 📈 Roadmap

### Versão 1.0 ✅ (Atual)
- [x] Estrutura base de 10 capítulos
- [x] Design moderno com glassmorphism
- [x] Capítulos 1 e 2 completos
- [x] Visualizações com Chart.js
- [x] Layout responsivo

### Versão 2.0 🚀 (Próxima)
- [ ] Sistema de busca global
- [ ] Modo escuro/claro
- [ ] Sistema de favoritos
- [ ] Progresso do usuário (LocalStorage)
- [ ] Quiz interativo por capítulo
- [ ] Calculadora estatística integrada
- [ ] PWA (funciona offline)
- [ ] Completar capítulos 3-10

### Versão 3.0 🔮 (Futuro)
- [ ] Backend com Node.js
- [ ] Sistema de login
- [ ] Fórum de discussão
- [ ] Certificados de conclusão
- [ ] Integração com R/Python para cálculos

## 🤝 Contribuindo

Contribuições são bem-vindas! Siga estes passos:

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/NovaFeature`)
3. Commit suas mudanças (`git commit -m 'Adiciona NovaFeature'`)
4. Push para a branch (`git push origin feature/NovaFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👥 Autores

- **Desenvolvimento Web** - Interface interativa e design
- **Conteúdo Base** - Larson & Farber (Estatística Aplicada, 6ª Ed.)

## 📞 Contato

Para dúvidas, sugestões ou feedback:
- 📧 Email: [seu-email@exemplo.com]
- 🐛 Issues: [GitHub Issues](link-do-repositorio/issues)

## 🙏 Agradecimentos

- Larson & Farber pelo excelente conteúdo do livro
- Chart.js pela biblioteca de gráficos
- Google Fonts pela tipografia
- Comunidade open source

---

**⭐ Se este projeto foi útil para você, considere dar uma estrela!**

**📚 Bons estudos de Estatística!**

---

<div align="center">
  <sub>Desenvolvido com ❤️ e ☕</sub>
</div>
