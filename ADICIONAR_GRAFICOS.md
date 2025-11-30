# 🎯 GUIA RÁPIDO: Adicionar Visualizações nos Capítulos 5, 9 e 10

## ⚡ INSTRUÇÕES RÁPIDAS

Para cada capítulo, faça 3 coisas:
1. Adicionar CDN do Chart.js no `<head>`
2. Adicionar container do gráfico na seção
3. Adicionar JavaScript antes do `</body>`

---

## 📊 CAPÍTULO 5 - DISTRIBUIÇÃO NORMAL

### 1. Adicionar no `<head>` (após as outras tags):
```html
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
```

### 2. Adicionar após a linha "Regra 68-95-99,7" (aproximadamente linha 110):
```html
<div class="chart-container" style="position: relative; height: 400px; margin: 2rem 0; background: white; padding: 1rem; border-radius: 10px;">
    <canvas id="normalCurveChart"></canvas>
</div>
```

### 3. Adicionar antes do `</body>` (após o script toggleSolution):
```javascript
// Gráfico da Distribuição Normal
const normalCtx = document.getElementById('normalCurveChart');
if (normalCtx) {
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
                legend: { display: false },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return 'Densidade: ' + context.parsed.y.toFixed(4);
                        }
                    }
                }
            },
            scales: {
                x: {
                    title: { 
                        display: true, 
                        text: 'Z (desvios padrão da média)',
                        font: { size: 14, weight: 'bold' }
                    },
                    grid: { color: 'rgba(0,0,0,0.1)' }
                },
                y: {
                    title: { 
                        display: true, 
                        text: 'Densidade de Probabilidade',
                        font: { size: 14, weight: 'bold' }
                    },
                    grid: { color: 'rgba(0,0,0,0.1)' }
                }
            }
        }
    });
}
```

---

## 📈 CAPÍTULO 9 - CORRELAÇÃO E REGRESSÃO

### 1. Adicionar no `<head>`:
```html
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
```

### 2. Adicionar na Seção 9.2 (após "Regressão Linear Simples"):
```html
<div class="chart-container" style="position: relative; height: 450px; margin: 2rem 0; background: white; padding: 1rem; border-radius: 10px;">
    <canvas id="regressionChart"></canvas>
</div>
```

### 3. Adicionar antes do `</body>`:
```javascript
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
                    fill: false,
                    borderDash: []
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
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            if (context.dataset.type === 'scatter') {
                                return `Horas: ${context.parsed.x}, Nota: ${context.parsed.y}`;
                            }
                            return context.dataset.label;
                        }
                    }
                }
            },
            scales: {
                x: {
                    title: { 
                        display: true, 
                        text: 'Horas de Estudo',
                        font: { size: 14, weight: 'bold' }
                    },
                    min: 0,
                    max: 12,
                    grid: { color: 'rgba(0,0,0,0.1)' }
                },
                y: {
                    title: { 
                        display: true, 
                        text: 'Nota no Teste',
                        font: { size: 14, weight: 'bold' }
                    },
                    min: 50,
                    max: 100,
                    grid: { color: 'rgba(0,0,0,0.1)' }
                }
            }
        }
    });
}
```

---

## 🎲 CAPÍTULO 10 - QUI-QUADRADO E ANOVA

### 1. Adicionar no `<head>`:
```html
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
```

### 2. Adicionar na Seção 10.1 (após o exemplo de Gênero vs Preferência):
```html
<div class="chart-container" style="position: relative; height: 400px; margin: 2rem 0; background: white; padding: 1rem; border-radius: 10px;">
    <canvas id="chiSquareChart"></canvas>
</div>
```

### 3. Adicionar antes do `</body>`:
```javascript
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
                    title: { 
                        display: true, 
                        text: 'Categoria',
                        font: { size: 14, weight: 'bold' }
                    }
                },
                y: {
                    title: { 
                        display: true, 
                        text: 'Frequência',
                        font: { size: 14, weight: 'bold' }
                    },
                    beginAtZero: true,
                    grid: { color: 'rgba(0,0,0,0.1)' }
                }
            }
        }
    });
}
```

---

## ✅ CHECKLIST DE IMPLEMENTAÇÃO

### Capítulo 5:
- [ ] CDN adicionado no `<head>`
- [ ] Container do gráfico adicionado
- [ ] JavaScript adicionado
- [ ] Testado em http://localhost:8000/chapter5.html

### Capítulo 9:
- [ ] CDN adicionado no `<head>`
- [ ] Container do gráfico adicionado
- [ ] JavaScript adicionado
- [ ] Testado em http://localhost:8000/chapter9.html

### Capítulo 10:
- [ ] CDN adicionado no `<head>`
- [ ] Container do gráfico adicionado
- [ ] JavaScript adicionado
- [ ] Testado em http://localhost:8000/chapter10.html

---

## 🎨 DICAS DE ESTILO

Os gráficos já estão estilizados com:
- ✅ Fundo branco com padding
- ✅ Bordas arredondadas
- ✅ Cores consistentes (#667eea azul, #ff6b6b vermelho)
- ✅ Títulos e legendas claras
- ✅ Responsivos
- ✅ Tooltips informativos

---

## 🚀 RESULTADO ESPERADO

Após adicionar, você terá:
- **Cap 5:** Curva normal interativa em sino
- **Cap 9:** Scatter plot com reta de regressão
- **Cap 10:** Barras comparativas (observado vs esperado)

---

## 💡 REFERÊNCIA

Veja todos os gráficos funcionando em:
**http://localhost:8000/visualizacoes_demo.html**

---

**Criado em:** 2025-11-29 09:07
**Status:** Códigos prontos para copiar e colar! ✅
