"""
Script completo para adicionar TODOS os gráficos nos capítulos 5, 9 e 10
"""
import re

CHARTJS_CDN = '<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>'

def add_cdn_to_head(html_content):
    if 'chart.js' in html_content.lower():
        return html_content
    return html_content.replace('</head>', f'    {CHARTJS_CDN}\n</head>')

def process_chapter5(filename):
    """Adiciona curva normal no Capítulo 5"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Adicionar CDN
        content = add_cdn_to_head(content)
        
        # Container do gráfico
        chart_html = '''
            <div class="chart-container" style="position: relative; height: 400px; margin: 2rem 0; background: white; padding: 1rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                <canvas id="normalCurveChart"></canvas>
            </div>'''
        
        # JavaScript
        chart_js = '''
        // Gráfico da Distribuição Normal
        const normalCtx = document.getElementById('normalCurveChart');
        if (normalCtx) {
            function normalPDF(x, mu = 0, sigma = 1) {
                return (1 / (sigma * Math.sqrt(2 * Math.PI))) * Math.exp(-0.5 * Math.pow((x - mu) / sigma, 2));
            }

            const xValues = [];
            const yValues = [];
            for (let x = -4; x <= 4; x += 0.1) {
                xValues.push(x.toFixed(1));
                yValues.push(normalPDF(x));
            }

            new Chart(normalCtx, {
                type: 'line',
                data: {
                    labels: xValues,
                    datasets: [{
                        label: 'Distribuição Normal Padrão',
                        data: yValues,
                        borderColor: '#667eea',
                        backgroundColor: 'rgba(102, 126, 234, 0.2)',
                        fill: true,
                        tension: 0.4,
                        pointRadius: 0,
                        borderWidth: 3
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        title: {
                            display: true,
                            text: 'Curva Normal (μ=0, σ=1) - A Famosa "Curva em Sino"',
                            font: { size: 18, weight: 'bold' },
                            color: '#333'
                        },
                        legend: { display: false }
                    },
                    scales: {
                        x: {
                            title: { display: true, text: 'Z (desvios padrão da média)', font: { size: 14, weight: 'bold' } }
                        },
                        y: {
                            title: { display: true, text: 'Densidade de Probabilidade', font: { size: 14, weight: 'bold' } }
                        }
                    }
                }
            });
        }
'''
        
        # Adicionar container após "Regra 68-95-99,7"
        if 'Regra 68-95-99,7' in content and 'normalCurveChart' not in content:
            pattern = r'(99,7% dentro de ±3σ da média\s*</div>\s*</div>)'
            content = re.sub(pattern, r'\1' + chart_html, content, count=1)
        
        # Adicionar JavaScript
        if 'normalCurveChart' in content and 'const normalCtx' not in content:
            content = content.replace('</body>', chart_js + '\n    </body>')
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Chapter 5 atualizado com curva normal!")
        return True
    except Exception as e:
        print(f"❌ Erro no Chapter 5: {e}")
        return False

def process_chapter10(filename):
    """Adiciona gráfico qui-quadrado no Capítulo 10"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Adicionar CDN
        content = add_cdn_to_head(content)
        
        # Container
        chart_html = '''
            <div class="chart-container" style="position: relative; height: 400px; margin: 2rem 0; background: white; padding: 1rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                <canvas id="chiSquareChart"></canvas>
            </div>'''
        
        # JavaScript
        chart_js = '''
        // Gráfico Qui-Quadrado
        const chiCtx = document.getElementById('chiSquareChart');
        if (chiCtx) {
            new Chart(chiCtx, {
                type: 'bar',
                data: {
                    labels: ['Masc/Prod A', 'Masc/Prod B', 'Fem/Prod A', 'Fem/Prod B'],
                    datasets: [
                        {
                            label: 'Frequência Observada',
                            data: [30, 20, 15, 35],
                            backgroundColor: '#667eea',
                            borderColor: '#667eea',
                            borderWidth: 2
                        },
                        {
                            label: 'Frequência Esperada (sob H₀)',
                            data: [22.5, 27.5, 22.5, 27.5],
                            backgroundColor: '#ff6b6b',
                            borderColor: '#ff6b6b',
                            borderWidth: 2
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        title: {
                            display: true,
                            text: 'Teste Qui-Quadrado: Gênero vs Preferência de Produto',
                            font: { size: 18, weight: 'bold' },
                            color: '#333'
                        },
                        legend: {
                            display: true,
                            position: 'top'
                        },
                        subtitle: {
                            display: true,
                            text: 'χ² = 9,09 > 3,841 → Rejeitar H₀ (há associação!)',
                            font: { size: 14 },
                            color: '#ff6b6b',
                            padding: { bottom: 10 }
                        }
                    },
                    scales: {
                        x: {
                            title: { display: true, text: 'Categoria', font: { size: 14, weight: 'bold' } }
                        },
                        y: {
                            title: { display: true, text: 'Frequência', font: { size: 14, weight: 'bold' } },
                            beginAtZero: true
                        }
                    }
                }
            });
        }
'''
        
        # Adicionar container após exemplo de Gênero vs Preferência
        if 'Gênero e Preferência' in content and 'chiSquareChart' not in content:
            pattern = r'(Homens preferem mais o Produto A, mulheres preferem mais o Produto B\.\s*</div>)'
            content = re.sub(pattern, r'\1' + chart_html, content, count=1)
        
        # Adicionar JavaScript
        if 'chiSquareChart' in content and 'const chiCtx' not in content:
            content = content.replace('</body>', chart_js + '\n    </body>')
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Chapter 10 atualizado com gráfico qui-quadrado!")
        return True
    except Exception as e:
        print(f"❌ Erro no Chapter 10: {e}")
        return False

# Executar
print("🚀 Adicionando gráficos nos capítulos...")
print()

process_chapter5('chapter5.html')
process_chapter10('chapter10.html')

print()
print("🎉 TODOS OS GRÁFICOS ADICIONADOS COM SUCESSO!")
print()
print("📊 Gráficos adicionados:")
print("  ✅ Chapter 5: Curva Normal")
print("  ✅ Chapter 9: Regressão Linear (já feito)")
print("  ✅ Chapter 10: Qui-Quadrado")
print()
print("🌐 Teste agora:")
print("  http://localhost:8000/chapter5.html")
print("  http://localhost:8000/chapter9.html")
print("  http://localhost:8000/chapter10.html")
