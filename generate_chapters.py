"""
Gerador Automático de Capítulos HTML
Este script cria páginas HTML completas para todos os capítulos do livro
"""

# Estrutura dos capítulos do livro (baseado no índice)
CHAPTERS = [
    {
        "number": 1,
        "title": "Introdução à Estatística",
        "subtitle": "Fundamentos essenciais para compreender e aplicar a estatística",
        "icon": "🎯"
    },
    {
        "number": 2,
        "title": "Estatística Descritiva",
        "subtitle": "Organize, resuma e apresente dados de forma significativa",
        "icon": "📊"
    },
    {
        "number": 3,
        "title": "Probabilidade",
        "subtitle": "Entenda e calcule a chance de eventos ocorrerem",
        "icon": "🎲"
    },
    {
        "number": 4,
        "title": "Distribuições de Probabilidade Discretas",
        "subtitle": "Binomial, Poisson e outras distribuições importantes",
        "icon": "📈"
    },
    {
        "number": 5,
        "title": "Distribuições de Probabilidade Normais",
        "subtitle": "A curva em sino e suas aplicações",
        "icon": "🔔"
    },
    {
        "number": 6,
        "title": "Intervalos de Confiança",
        "subtitle": "Estime parâmetros populacionais com precisão",
        "icon": "🎯"
    },
    {
        "number": 7,
        "title": "Teste de Hipótese com Uma Amostra",
        "subtitle": "Tome decisões baseadas em evidências estatísticas",
        "icon": "⚖️"
    },
    {
        "number": 8,
        "title": "Teste de Hipótese com Duas Amostras",
        "subtitle": "Compare dois grupos e tire conclusões",
        "icon": "🔬"
    },
    {
        "number": 9,
        "title": "Correlação e Regressão",
        "subtitle": "Descubra relações entre variáveis",
        "icon": "📉"
    },
    {
        "number": 10,
        "title": "Teste Qui-Quadrado e Distribuição F",
        "subtitle": "Testes para dados categóricos e variâncias",
        "icon": "χ²"
    }
]

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Capítulo {number} - {title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/chapter.css">
</head>
<body>
    <nav class="top-nav">
        <a href="{prev_link}" class="back-btn">← Capítulo Anterior</a>
        <div class="nav-title">Capítulo {number}</div>
        <a href="{next_link}" class="next-btn">Próximo Capítulo →</a>
    </nav>

    <div class="chapter-container">
        <section class="chapter-hero">
            <div class="hero-badge">Capítulo {number}</div>
            <h1 class="chapter-title">{title}</h1>
            <p class="chapter-subtitle">{subtitle}</p>
        </section>

        <section class="content-section intro-section">
            <div class="section-icon">{icon}</div>
            <h2>Bem-vindo ao Capítulo {number}</h2>
            <p class="lead-text">
                Este capítulo aborda <strong>{title}</strong>, um tópico fundamental em estatística.
                Você aprenderá conceitos essenciais, verá exemplos práticos e resolverá exercícios
                que consolidarão seu aprendizado.
            </p>
            <div class="highlight-box">
                <h3>💡 O que você aprenderá</h3>
                <ul>
                    <li>Conceitos fundamentais e definições importantes</li>
                    <li>Fórmulas e cálculos passo a passo</li>
                    <li>Aplicações práticas no mundo real</li>
                    <li>Exercícios resolvidos detalhadamente</li>
                </ul>
            </div>
        </section>

        <section class="content-section">
            <h2>📚 Conteúdo em Desenvolvimento</h2>
            <p>
                Este capítulo está sendo desenvolvido com conteúdo rico e interativo.
                Em breve você terá acesso a:
            </p>
            <ul>
                <li>Explicações detalhadas de todos os conceitos</li>
                <li>Exemplos resolvidos passo a passo</li>
                <li>Gráficos e visualizações interativas</li>
                <li>Exercícios práticos com soluções completas</li>
                <li>Aplicações do mundo real</li>
            </ul>
            <div class="tip-box">
                <h3>💡 Enquanto isso...</h3>
                <p>
                    Você pode estudar os capítulos anteriores ou consultar o livro texto
                    "Estatística Aplicada" de Larson & Farber (6ª Edição) para este conteúdo.
                </p>
            </div>
        </section>

        <div class="chapter-nav-footer">
            <a href="{prev_link}" class="nav-btn prev-btn">
                <span>←</span>
                <div>
                    <div class="nav-label">Anterior</div>
                    <div class="nav-title">{prev_title}</div>
                </div>
            </a>
            <a href="{next_link}" class="nav-btn next-btn">
                <div>
                    <div class="nav-label">Próximo</div>
                    <div class="nav-title">{next_title}</div>
                </div>
                <span>→</span>
            </a>
        </div>
    </div>

    <script>
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {{
            anchor.addEventListener('click', function (e) {{
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {{
                    target.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
                }}
            }});
        }});
    </script>
</body>
</html>"""

def generate_all_chapters():
    """Gera arquivos HTML para todos os capítulos"""
    print("🚀 Gerando páginas HTML para todos os capítulos...")
    print(f"📚 Total de capítulos: {len(CHAPTERS)}\n")
    
    for i, chapter in enumerate(CHAPTERS):
        # Determinar links anteriores e próximos
        prev_link = f"chapter{i}.html" if i > 0 else "index.html"
        next_link = f"chapter{i+2}.html" if i < len(CHAPTERS) - 1 else "index.html"
        
        prev_title = f"Capítulo {i}" if i > 0 else "Início"
        next_title = f"Capítulo {i+2}" if i < len(CHAPTERS) - 1 else "Início"
        
        # Gerar HTML
        html_content = HTML_TEMPLATE.format(
            number=chapter['number'],
            title=chapter['title'],
            subtitle=chapter['subtitle'],
            icon=chapter['icon'],
            prev_link=prev_link,
            next_link=next_link,
            prev_title=prev_title,
            next_title=next_title
        )
        
        # Salvar arquivo
        filename = f"chapter{chapter['number']}.html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ Criado: {filename} - {chapter['title']}")
    
    print(f"\n🎉 Todos os {len(CHAPTERS)} capítulos foram gerados com sucesso!")
    print("\n📝 Próximos passos:")
    print("1. Abra http://localhost:8000 no navegador")
    print("2. Clique em 'Começar a Estudar'")
    print("3. Navegue pelos capítulos")
    print("\n💡 Os Capítulos 1 e 2 já têm conteúdo completo!")
    print("   Os demais capítulos mostram a estrutura e serão preenchidos gradualmente.")

if __name__ == "__main__":
    generate_all_chapters()
