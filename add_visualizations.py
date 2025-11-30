"""
Script para adicionar visualizações Chart.js a todos os capítulos
Adiciona gráficos interativos onde fazem mais sentido
"""

import re

# Mapeamento de visualizações por capítulo
VISUALIZATIONS = {
    'chapter5.html': {
        'cdn': '<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>',
        'charts': [
            {
                'position': 'after_line_containing': 'Regra 68-95-99,7',
                'html': '''
            <div class="chart-container" style="position: relative; height: 400px; margin: 2rem 0;">
                <canvas id="normalCurveChart"></canvas>
            </div>''',
                'script': '''
        // Distribuição Normal
        const normalCtx = document.getElementById('normalCurveChart').getContext('2d');
        
        function normalPDF(x, mu = 0, sigma = 1) {
            return (1 / (sigma * Math.sqrt(2 * Math.PI))) * 
                   Math.exp(-0.5 * Math.pow((x - mu) / sigma, 2));
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
                    backgroundColor: 'rgba(102, 126, 234, 0.1)',
                    fill: true,
                    tension: 0.4,
                    pointRadius: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    title: {
                        display: true,
                        text: 'Curva Normal (μ=0, σ=1)',
                        font: { size: 16, weight: 'bold' }
                    },
                    legend: { display: false }
                },
                scales: {
                    x: {
                        title: { display: true, text: 'Z (desvios padrão da média)' }
                    },
                    y: {
                        title: { display: true, text: 'Densidade de Probabilidade' }
                    }
                }
            }
        });
'''
            }
        ]
    },
    
    'chapter9.html': {
        'cdn': '<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>',
        'charts': [
            {
                'position': 'after_line_containing': 'Regressão Linear Simples',
                'html': '''
            <div class="chart-container" style="position: relative; height: 400px; margin: 2rem 0;">
                <canvas id="regressionChart"></canvas>
            </div>''',
                'script': '''
        // Regressão Linear
        const regCtx = document.getElementById('regressionChart').getContext('2d');
        
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
                        label: 'Dados Observados',
                        data: studyData,
                        backgroundColor: '#667eea',
                        pointRadius: 8,
                        pointHoverRadius: 10
                    },
                    {
                        label: 'Reta de Regressão: ŷ = 59,5 + 3,75x',
                        data: regressionLine,
                        type: 'line',
                        borderColor: '#ff6b6b',
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
                        text: 'Horas de Estudo vs Nota (r = 0,985)',
                        font: { size: 16, weight: 'bold' }
                    }
                },
                scales: {
                    x: {
                        title: { display: true, text: 'Horas de Estudo' },
                        min: 0,
                        max: 12
                    },
                    y: {
                        title: { display: true, text: 'Nota' },
                        min: 50,
                        max: 100
                    }
                }
            }
        });
'''
            }
        ]
    }
}

print("Script de visualizações criado!")
print("Para adicionar manualmente:")
print("1. Adicione o CDN do Chart.js no <head>")
print("2. Adicione os containers de canvas nas seções")
print("3. Adicione os scripts antes do </body>")
