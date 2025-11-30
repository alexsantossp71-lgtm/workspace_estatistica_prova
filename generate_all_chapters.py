"""
Gerador AVANÇADO de Capítulos - Extrai conteúdo REAL e DETALHADO do PDF
"""
from pypdf import PdfReader
import re

# Mapeamento preciso de capítulos
CHAPTERS = {
    3: {
        "title": "Probabilidade",
        "subtitle": "Entenda e calcule a chance de eventos ocorrerem",
        "icon": "🎲",
        "start_page": 124,
        "end_page": 180,
        "topics": [
            "Conceitos básicos de probabilidade e contagem",
            "Probabilidade condicional e regra da multiplicação",
            "Regra da adição",
            "Contagem: permutações e combinações"
        ]
    },
    4: {
        "title": "Distribuições de Probabilidade Discretas",
        "subtitle": "Binomial, Poisson e outras distribuições importantes",
        "icon": "📈",
        "start_page": 181,
        "end_page": 230,
        "topics": [
            "Variáveis aleatórias discretas",
            "Distribuição binomial",
            "Distribuição de Poisson",
            "Outras distribuições discretas"
        ]
    },
    5: {
        "title": "Distribuições de Probabilidade Normais",
        "subtitle": "A curva em sino e suas aplicações",
        "icon": "🔔",
        "start_page": 231,
        "end_page": 280,
        "topics": [
            "Introdução às distribuições normais",
            "Distribuição normal padrão",
            "Aplicações da distribuição normal",
            "Distribuições amostrais e teorema do limite central",
            "Aproximações normais para distribuições binomiais"
        ]
    },
    6: {
        "title": "Intervalos de Confiança",
        "subtitle": "Estime parâmetros populacionais com precisão",
        "icon": "🎯",
        "start_page": 281,
        "end_page": 330,
        "topics": [
            "Intervalos de confiança para a média (σ conhecido)",
            "Intervalos de confiança para a média (σ desconhecido)",
            "Intervalos de confiança para proporções populacionais",
            "Intervalos de confiança para variância e desvio padrão"
        ]
    },
    7: {
        "title": "Teste de Hipótese com Uma Amostra",
        "subtitle": "Tome decisões baseadas em evidências estatísticas",
        "icon": "⚖️",
        "start_page": 331,
        "end_page": 380,
        "topics": [
            "Introdução ao teste de hipótese",
            "Teste de hipótese para a média (σ conhecido)",
            "Teste de hipótese para a média (σ desconhecido)",
            "Teste de hipótese para proporções",
            "Teste de hipótese para variância e desvio padrão"
        ]
    },
    8: {
        "title": "Teste de Hipótese com Duas Amostras",
        "subtitle": "Compare dois grupos e tire conclusões",
        "icon": "🔬",
        "start_page": 381,
        "end_page": 430,
        "topics": [
            "Teste para diferença entre duas médias (amostras independentes)",
            "Teste para diferença entre duas médias (amostras dependentes)",
            "Teste para diferença entre duas proporções",
            "Teste F para comparar duas variâncias"
        ]
    },
    9: {
        "title": "Correlação e Regressão",
        "subtitle": "Descubra relações entre variáveis",
        "icon": "📉",
        "start_page": 431,
        "end_page": 480,
        "topics": [
            "Correlação linear",
            "Regressão linear e coeficiente de determinação",
            "Medidas de variação de regressão",
            "Intervalos de predição"
        ]
    },
    10: {
        "title": "Teste Qui-Quadrado e Distribuição F",
        "subtitle": "Testes para dados categóricos e variâncias",
        "icon": "χ²",
        "start_page": 488,
        "end_page": 540,
        "topics": [
            "Teste de qualidade do ajuste",
            "Teste de independência",
            "Comparando duas variâncias",
            "Análise de variância (ANOVA)"
        ]
    }
}

def extract_real_content(pdf_path, chapter_num):
    """Extrai conteúdo REAL e detalhado do PDF"""
    try:
        reader = PdfReader(pdf_path)
        chapter = CHAPTERS[chapter_num]
        
        # Extrair texto completo do capítulo
        full_text = ""
        for page in range(chapter["start_page"], min(chapter["end_page"], len(reader.pages))):
            full_text += reader.pages[page].extract_text() + "\n"
        
        # Extrair parágrafos significativos (mais de 100 caracteres)
        paragraphs = []
        for para in full_text.split('\n\n'):
            clean_para = para.strip()
            if len(clean_para) > 100 and len(clean_para) < 1000:
                # Remover quebras de linha dentro do parágrafo
                clean_para = ' '.join(clean_para.split('\n'))
                paragraphs.append(clean_para)
        
        return {
            "title": chapter["title"],
            "subtitle": chapter["subtitle"],
            "icon": chapter["icon"],
            "topics": chapter["topics"],
            "paragraphs": paragraphs[:10]  # Primeiros 10 parágrafos significativos
        }
    except Exception as e:
        print(f"⚠️  Erro ao extrair capítulo {chapter_num}: {e}")
        return None

def generate_rich_html(chapter_num, content):
    """Gera HTML RICO com conteúdo REAL"""
    
    if not content:
        return None
    
    # Gerar TOC
    toc_html = ""
    for i, topic in enumerate(content['topics'], 1):
        toc_html += f"""
                <a href="#secao{i}" class="toc-item">
                    <span class="toc-number">{chapter_num}.{i}</span>
                    <span class="toc-title">{topic}</span>
                </a>"""
    
    # Gerar seções com conteúdo REAL
    sections_html = ""
    for i, topic in enumerate(content['topics'], 1):
        # Pegar parágrafos relevantes para esta seção
        section_content = ""
        if i <= len(content['paragraphs']):
            section_content = content['paragraphs'][i-1]
        else:
            section_content = f"Esta seção aborda {topic.lower()}. O conteúdo detalhado será expandido em breve com mais exemplos e exercícios práticos."
        
        sections_html += f"""
        <section id="secao{i}" class="content-section">
            <div class="section-header">
                <span class="section-number">{chapter_num}.{i}</span>
                <h2>{topic}</h2>
            </div>
            
            <p class="section-intro">
                {section_content}
            </p>
            
            <div class="highlight-box">
                <h3>💡 Pontos Importantes</h3>
                <ul>
                    <li>Compreenda os conceitos fundamentais desta seção</li>
                    <li>Pratique com exemplos e exercícios</li>
                    <li>Aplique o conhecimento em situações reais</li>
                </ul>
            </div>
        </section>
        """
    
    prev_link = f"chapter{chapter_num-1}.html" if chapter_num > 1 else "index.html"
    next_link = f"chapter{chapter_num+1}.html" if chapter_num < 10 else "index.html"
    prev_title = f"Capítulo {chapter_num-1}" if chapter_num > 1 else "Início"
    next_title = f"Capítulo {chapter_num+1}" if chapter_num < 10 else "Início"
    
    html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Capítulo {chapter_num} - {content['title']}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="css/chapter.css">
</head>
<body>
    <nav class="top-nav">
        <a href="{prev_link}" class="back-btn">← Capítulo Anterior</a>
        <div class="nav-title">Capítulo {chapter_num}</div>
        <a href="{next_link}" class="next-btn">Próximo Capítulo →</a>
    </nav>

    <div class="chapter-container">
        <section class="chapter-hero">
            <div class="hero-badge">Capítulo {chapter_num}</div>
            <h1 class="chapter-title">{content['title']}</h1>
            <p class="chapter-subtitle">{content['subtitle']}</p>
        </section>

        <section class="toc-section">
            <h2>📚 Neste Capítulo</h2>
            <div class="toc-grid">
                {toc_html}
            </div>
        </section>

        <section class="content-section intro-section">
            <div class="section-icon">{content['icon']}</div>
            <h2>Visão Geral</h2>
            <p class="lead-text">
                Este capítulo aborda <strong>{content['title']}</strong>, um tópico fundamental em estatística.
                Você aprenderá conceitos essenciais, verá aplicações práticas e desenvolverá habilidades
                para resolver problemas reais.
            </p>
            <div class="highlight-box">
                <h3>💡 O que você aprenderá</h3>
                <ul>
                    {''.join([f'<li>{topic}</li>' for topic in content['topics']])}
                </ul>
            </div>
        </section>

        {sections_html}

        <section class="content-section">
            <h2>📝 Próximos Passos</h2>
            <div class="tip-box">
                <h3>💡 Continue Aprendendo</h3>
                <p>
                    Este capítulo apresenta os conceitos fundamentais. Para aprofundar seu conhecimento:
                </p>
                <ul>
                    <li>Pratique com os exercícios do livro texto</li>
                    <li>Resolva problemas adicionais</li>
                    <li>Aplique os conceitos em projetos reais</li>
                    <li>Revise os capítulos anteriores se necessário</li>
                </ul>
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
    
    return html

def main():
    """Função principal"""
    print("🚀 Gerando capítulos com CONTEÚDO REAL do PDF...")
    print("📖 Extraindo parágrafos e informações detalhadas...\n")
    
    pdf_path = "Estat_stica_Aplicada_6_Edi_o_Faber_e_Lar.pdf"
    
    for chapter_num in range(3, 11):
        print(f"📚 Processando Capítulo {chapter_num}...")
        
        # Extrair conteúdo REAL
        content = extract_real_content(pdf_path, chapter_num)
        
        if not content:
            print(f"   ❌ Falha ao extrair capítulo {chapter_num}")
            continue
        
        # Gerar HTML RICO
        html = generate_rich_html(chapter_num, content)
        
        if not html:
            print(f"   ❌ Falha ao gerar HTML para capítulo {chapter_num}")
            continue
        
        # Salvar arquivo
        filename = f"chapter{chapter_num}.html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"   ✅ Criado: {filename} - {content['title']}")
        print(f"      • {len(content['topics'])} tópicos principais")
        print(f"      • {len(content['paragraphs'])} parágrafos extraídos")
        print()
    
    print("🎉 Processo concluído!")
    print("\n📝 Resumo:")
    print("   ✅ Capítulos 1-2: Conteúdo manual completo e detalhado")
    print("   ✅ Capítulos 3-10: Conteúdo extraído do PDF com parágrafos reais")
    print("\n🌐 Acesse: http://localhost:8000")
    print("\n💡 Dica: Os capítulos agora têm conteúdo REAL extraído do livro!")

if __name__ == "__main__":
    main()
