import os

def add_saiba_mais_to_v2():
    base_dir = r"f:\workspace_estatistica_prova"
    
    # Data for each chapter
    videos_data = {
        1: [
            ("População e Amostra", "Prof. Enildo Barbosa", "Conceitos de população, amostra e tipos de amostras"),
            ("Tipos de Dados em Estatística", "Prof. Alexandre Patriota", "Dados qualitativos e quantitativos"),
            ("Introdução à Estatística", "UNIVESP", "Termos estatísticos principais e conceitos fundamentais")
        ],
        2: [
            ("Medidas de Tendência Central", "Matemática Rio", "Média, mediana, moda, variância e desvio padrão"),
            ("Média, Mediana e Moda", "Prof. Ferretto", "Como calcular e quando usar cada medida"),
            ("Medidas de Dispersão", "Me Salva!", "Variância, desvio padrão e coeficiente de variação")
        ],
        3: [
            ("Probabilidade Condicional", "Aplicadas Descomplicadas", "Definição, fórmulas e exercícios"),
            ("Teorema de Bayes", "Responde Aí", "Relação com probabilidade condicional e aplicações"),
            ("Probabilidade e Árvores", "Khan Academy", "Diagramas de árvore e exemplos práticos")
        ],
        4: [
            ("Distribuição Binomial", "Estatística Básica", "Definição e aplicação dos 4 critérios"),
            ("Distribuição de Poisson", "Prof. Grings", "Definição, fórmula e exercícios resolvidos"),
            ("Variáveis Aleatórias Discretas", "USP", "Conceitos fundamentais e distribuições")
        ],
        5: [
            ("Distribuição Normal", "Estatística para Todos", "A curva em sino e suas propriedades"),
            ("Como usar a Tabela Z", "Prof. Guru", "Encontrando probabilidades na tabela normal"),
            ("Regra Empírica 68-95-99.7", "Khan Academy", "Entendendo os desvios padrão na normal")
        ],
        6: [
            ("Intervalos de Confiança", "The Friendly Statistician", "Como calcular e interpretar"),
            ("Intervalo de Confiança para Média", "Statplace", "Exemplos práticos passo a passo"),
            ("Distribuição T de Student", "Khan Academy", "Quando usar T em vez de Z")
        ],
        7: [
            ("Teste de Hipótese", "Prof. Alex Santos", "Hipótese nula vs alternativa"),
            ("Entendendo o P-valor", "Khan Academy", "Interpretação intuitiva da significância"),
            ("Erros Tipo I e II", "Prof. Fernanda Maciel", "Consequências das decisões estatísticas")
        ],
        8: [
            ("Teste de Hipótese 2 Amostras", "Estatística Fácil", "Comparando duas médias populacionais"),
            ("Amostras Dependentes vs Independentes", "Me Salva!", "Diferenças e testes pareados"),
            ("Teste para Proporções", "Prof. Grings", "Comparação de duas proporções")
        ],
        9: [
            ("Correlação Linear", "Estatística com R", "Força e direção da associação (Pearson)"),
            ("Regressão Linear Simples", "Prof. Aquino", "Modelagem e previsão com reta de ajuste"),
            ("Coeficiente R²", "Khan Academy", "O que o R-quadrado nos diz sobre o modelo")
        ],
        10: [
            ("Teste Qui-Quadrado", "PsicoEstatística", "Teste de independência e aderência"),
            ("ANOVA de um fator", "Prof. Bolfarine", "Comparação de múltiplas médias"),
            ("Distribuição F", "Khan Academy", "Entendendo a razão de variâncias")
        ]
    }

    card_colors = [
        "linear-gradient(135deg, #667eea 0%, #764ba2 100%)", # Purple
        "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)", # Pink/Red
        "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)"  # Blue
    ]

    for i in range(1, 11):
        filename = f"chapter{i}_v2.html"
        filepath = os.path.join(base_dir, filename)

        if not os.path.exists(filepath):
            print(f"Skipping {filename} (not found)")
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if already added
        if "Saiba Mais" in content and "section-icon" in content:
             # Simple check to avoid duplication if run multiple times
             # But since we just created them, they shouldn't have it.
             # However, if I run this script twice, I should be careful.
             if 'id="saiba-mais-section"' in content:
                 print(f"Skipping {filename} (already has Saiba Mais)")
                 continue

        # Generate HTML for videos
        videos_html = ""
        chapter_videos = videos_data.get(i, [])
        
        for idx, (title, author, desc) in enumerate(chapter_videos):
            color = card_colors[idx % 3]
            search_query = f"{title} {author} estatistica".replace(" ", "+")
            url = f"https://www.youtube.com/results?search_query={search_query}"
            
            videos_html += f"""
        <div style="background: {color}; border-radius: 12px; padding: 1.5rem; color: white; box-shadow: 0 4px 6px rgba(0,0,0,0.1); transition: transform 0.3s ease;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
            <h4 style="margin: 0 0 0.5rem 0; font-size: 1.1rem; color: white;">📺 {title}</h4>
            <p style="margin: 0 0 1rem 0; font-size: 0.9rem; opacity: 0.9; color: rgba(255,255,255,0.9);">{author}</p>
            <p style="margin: 0 0 1rem 0; font-size: 0.85rem; color: rgba(255,255,255,0.8);">{desc}</p>
            <a href="{url}" target="_blank" style="display: inline-block; background: white; color: #333; padding: 0.5rem 1rem; border-radius: 20px; text-decoration: none; font-weight: 600; font-size: 0.85rem; transition: background 0.2s;">
                ▶️ Assistir no YouTube
            </a>
        </div>"""

        section_html = f"""
        <!-- SAIBA MAIS -->
        <section id="saiba-mais-section" class="content-section" style="margin-top: 3rem;">
            <div class="section-icon">🎥</div>
            <h2>Saiba Mais</h2>
            
            <p class="lead-text">
                Aprofunde seus conhecimentos com estes vídeos educativos selecionados sobre os temas deste capítulo:
            </p>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; margin-top: 2rem;">
                {videos_html}
            </div>

            <div class="tip-box" style="margin-top: 2rem;">
                <h3>💡 Dica de Estudo</h3>
                <p>
                    Assista aos vídeos para reforçar o aprendizado! Cada professor tem uma abordagem diferente que pode ajudar a consolidar os conceitos apresentados neste capítulo.
                </p>
            </div>
        </section>
        """

        # Insertion logic: Before the closing div of chapter-container
        # The chapter container usually ends before the script tags.
        # We look for the last </div> before <script> or before </body>
        
        # A robust way for these specific files:
        # Find the last occurrence of </div> that closes the container.
        # Since the file structure is consistent (from my previous generation), 
        # it ends with:
        #     </div>
        #     <script>...
        
        # Let's try to split by </div> and insert before the last one that is followed by <script or <a href="index_v2
        
        # Robust insertion logic
        # We want to insert before the closing </div> of .chapter-container
        # This div is typically the last div before the inline <script> tag at the bottom.
        
        # Split by the specific inline script start if possible, or just the last script tag
        if '<script>' in content:
            # Find the last <script> tag index
            last_script_idx = content.rfind('<script>')
            
            if last_script_idx != -1:
                # Content before the last script
                pre_script = content[:last_script_idx]
                post_script = content[last_script_idx:]
                
                # Find the last </div> in the pre_script part
                last_div_idx = pre_script.rfind('</div>')
                
                if last_div_idx != -1:
                    # Insert BEFORE this last div (which closes chapter-container)
                    # But wait, we want to insert INSIDE the chapter-container, so BEFORE the closing </div>?
                    # Yes.
                    # ... content ... [INSERT HERE] </div> <script> ...
                    
                    new_content = pre_script[:last_div_idx] + section_html + "\n" + pre_script[last_div_idx:] + post_script
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Added Saiba Mais to {filename}")
                else:
                    print(f"Could not find closing div in {filename}")
            else:
                print(f"Could not find script tag in {filename}")
        else:
             print(f"No script tag found in {filename}")

if __name__ == "__main__":
    add_saiba_mais_to_v2()
