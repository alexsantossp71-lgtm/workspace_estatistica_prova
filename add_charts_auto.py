"""
Script para adicionar visualizações Chart.js automaticamente nos capítulos
"""
import re

# CDN do Chart.js
CHARTJS_CDN = '<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>'

# Função para adicionar CDN no head
def add_cdn_to_head(html_content):
    if 'chart.js' in html_content.lower():
        return html_content
    
    # Adicionar antes do </head>
    return html_content.replace('</head>', f'    {CHARTJS_CDN}\n</head>')

# Função para adicionar gráfico de regressão no Cap 9
def add_regression_chart(html_content):
    # Container do gráfico
    chart_html = '''
            <div class="chart-container" style="position: relative; height: 450px; margin: 2rem 0; background: white; padding: 1rem; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                <canvas id="regressionChart"></canvas>
            </div>'''
    
    # JavaScript do gráfico
    chart_js = '''
        // Gráfico de Regressão Linear
        const regCtx = document.getElementById('regressionChart');
        if (regCtx) {
            const studyData = [
                { x: 2, y: 65 },
                { x: 4, y: 75 },
                { x: 6, y: 85 },
                { x: 8, y: 90 },
                { x: 10, y: 95 }
            ];

            const regressionLine = [];
            for (let x = 0; x <= 12; x += 0.5) {
                regressionLine.push({ x: x, y: 59.5 + 3.75 * x });
            }

            new Chart(regCtx, {
                type: 'scatter',
                data: {
                    datasets: [
                        {
                            label: 'Dados Observados (Alunos)',
                            data: studyData,
                            backgroundColor: '#667eea',
                            pointRadius: 10,
                            pointHoverRadius: 12,
                            pointBorderColor: '#fff',
                            pointBorderWidth: 2
                        },
                        {
                            label: 'Reta de Regressão: ŷ = 59,5 + 3,75x',
                            data: regressionLine,
                            type: 'line',
                            borderColor: '#ff6b6b',
                            backgroundColor: 'rgba(255, 107, 107, 0.1)',
                            borderWidth: 3,
                            pointRadius: 0,
                            fill: false
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        title: {
                            display: true,
                            text: 'Horas de Estudo vs Nota (r = 0,985 | R² = 97%)',
                            font: { size: 18, weight: 'bold' },
                            color: '#333'
                        },
                        legend: {
                            display: true,
                            position: 'top'
                        }
                    },
                    scales: {
                        x: {
                            title: { display: true, text: 'Horas de Estudo', font: { size: 14, weight: 'bold' } },
                            min: 0,
                            max: 12
                        },
                        y: {
                            title: { display: true, text: 'Nota no Teste', font: { size: 14, weight: 'bold' } },
                            min: 50,
                            max: 100
                        }
                    }
                }
            });
        }
'''
    
    # Adicionar container após "Regressão Linear Simples"
    if 'Regressão Linear Simples' in html_content and 'regressionChart' not in html_content:
        # Encontrar posição após o título da seção 9.2
        pattern = r'(<h2>Regressão Linear Simples</h2>\s*</div>)'
        html_content = re.sub(pattern, r'\1' + chart_html, html_content, count=1)
    
    # Adicionar JavaScript antes do </body>
    if 'regressionChart' in html_content and 'const regCtx' not in html_content:
        html_content = html_content.replace('</body>', chart_js + '\n    </body>')
    
    return html_content

# Processar chapter9.html
try:
    with open('chapter9.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = add_cdn_to_head(content)
    content = add_regression_chart(content)
    
    with open('chapter9.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Chapter 9 atualizado com gráfico de regressão!")
except Exception as e:
    print(f"❌ Erro no Chapter 9: {e}")

print("\n🎉 Script concluído!")
