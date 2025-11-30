"""
Script de Revisão Completa de TODOS os Capítulos
Verifica: integridade HTML, tamanho, conteúdo, seções, exercícios
"""
import os
import re

def analyze_chapter(filename):
    """Analisa um capítulo em detalhes"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verificações básicas
        has_doctype = '<!DOCTYPE html>' in content
        has_head = '<head>' in content
        has_body = '<body>' in content
        has_closing = '</html>' in content
        
        # Conteúdo
        has_toc = 'toc-section' in content or 'Neste Capítulo' in content
        has_exercises = 'exerc' in content.lower() or 'exercise' in content.lower()
        has_examples = 'exemplo' in content.lower() or 'example' in content.lower()
        has_formulas = 'formula' in content.lower() or 'fórmula' in content.lower()
        
        # Contar seções
        sections = len(re.findall(r'<h2>', content))
        subsections = len(re.findall(r'<h3>', content))
        
        # Contar exercícios
        exercise_blocks = len(re.findall(r'exercise-block|exercício', content, re.IGNORECASE))
        
        # Verificar se tem conteúdo real ou apenas placeholder
        has_placeholder = 'placeholder' in content.lower() or 'lorem ipsum' in content.lower()
        has_real_content = len(content) > 10000  # Mais de 10KB geralmente indica conteúdo real
        
        # Verificar gráficos
        has_chartjs = 'chart.js' in content.lower()
        chart_ids = re.findall(r'id="(\w*[Cc]hart\w*)"', content)
        
        return {
            'valid': has_doctype and has_head and has_body and has_closing,
            'size': len(content),
            'sections': sections,
            'subsections': subsections,
            'has_toc': has_toc,
            'has_exercises': has_exercises,
            'exercise_count': exercise_blocks,
            'has_examples': has_examples,
            'has_formulas': has_formulas,
            'has_placeholder': has_placeholder,
            'has_real_content': has_real_content,
            'has_chartjs': has_chartjs,
            'charts': chart_ids,
            'content_preview': content[:500] if len(content) > 500 else content
        }
    except Exception as e:
        return {'valid': False, 'error': str(e)}

# Lista de capítulos
chapters = [
    {'file': 'chapter1.html', 'title': 'Introdução à Estatística'},
    {'file': 'chapter2.html', 'title': 'Estatística Descritiva'},
    {'file': 'chapter3.html', 'title': 'Probabilidade'},
    {'file': 'chapter4.html', 'title': 'Distribuições Discretas'},
    {'file': 'chapter5.html', 'title': 'Distribuição Normal'},
    {'file': 'chapter6.html', 'title': 'Intervalos de Confiança'},
    {'file': 'chapter7.html', 'title': 'Teste de Hipótese (1 amostra)'},
    {'file': 'chapter8.html', 'title': 'Teste de Hipótese (2 amostras)'},
    {'file': 'chapter9.html', 'title': 'Correlação e Regressão'},
    {'file': 'chapter10.html', 'title': 'Qui-Quadrado e ANOVA'}
]

print("=" * 80)
print("📚 REVISÃO COMPLETA DE TODOS OS CAPÍTULOS")
print("=" * 80)
print()

results = []

for i, chapter in enumerate(chapters, 1):
    filename = chapter['file']
    title = chapter['title']
    
    print(f"📖 Capítulo {i}: {title}")
    print(f"   Arquivo: {filename}")
    
    if not os.path.exists(filename):
        print(f"   ❌ ARQUIVO NÃO ENCONTRADO!")
        results.append({
            'number': i,
            'title': title,
            'file': filename,
            'status': 'NOT_FOUND'
        })
        print()
        continue
    
    analysis = analyze_chapter(filename)
    
    if not analysis.get('valid', False):
        print(f"   ❌ HTML CORROMPIDO")
        print(f"   Erro: {analysis.get('error', 'Estrutura HTML inválida')}")
        results.append({
            'number': i,
            'title': title,
            'file': filename,
            'status': 'CORRUPTED',
            'size': analysis.get('size', 0)
        })
        print()
        continue
    
    # Determinar qualidade do conteúdo
    size = analysis['size']
    has_real = analysis['has_real_content']
    has_ex = analysis['has_exercises']
    ex_count = analysis['exercise_count']
    sections = analysis['sections']
    
    if size < 5000:
        quality = "❌ VAZIO/BÁSICO"
        status = "EMPTY"
    elif size < 15000:
        quality = "⚠️ INCOMPLETO"
        status = "INCOMPLETE"
    elif size < 25000:
        quality = "✅ BOM"
        status = "GOOD"
    else:
        quality = "✅ COMPLETO"
        status = "COMPLETE"
    
    print(f"   Qualidade: {quality}")
    print(f"   Tamanho: {size:,} bytes ({size/1024:.1f} KB)")
    print(f"   Seções: {sections} | Subseções: {analysis['subsections']}")
    print(f"   Exercícios: {'✅' if has_ex else '❌'} ({ex_count} blocos)")
    print(f"   Exemplos: {'✅' if analysis['has_examples'] else '❌'}")
    print(f"   Fórmulas: {'✅' if analysis['has_formulas'] else '❌'}")
    print(f"   TOC: {'✅' if analysis['has_toc'] else '❌'}")
    print(f"   Gráficos: {'✅ ' + str(len(analysis['charts'])) if analysis['charts'] else '❌'}")
    
    results.append({
        'number': i,
        'title': title,
        'file': filename,
        'status': status,
        'quality': quality,
        'size': size,
        'sections': sections,
        'exercises': ex_count,
        'has_examples': analysis['has_examples'],
        'has_formulas': analysis['has_formulas'],
        'charts': len(analysis['charts'])
    })
    print()

# Resumo geral
print("=" * 80)
print("📊 RESUMO GERAL")
print("=" * 80)
print()

total = len(results)
complete = sum(1 for r in results if r.get('status') == 'COMPLETE')
good = sum(1 for r in results if r.get('status') == 'GOOD')
incomplete = sum(1 for r in results if r.get('status') == 'INCOMPLETE')
empty = sum(1 for r in results if r.get('status') == 'EMPTY')
corrupted = sum(1 for r in results if r.get('status') == 'CORRUPTED')
not_found = sum(1 for r in results if r.get('status') == 'NOT_FOUND')

print(f"Total de capítulos: {total}")
print(f"  ✅ Completos (>25KB): {complete}")
print(f"  ✅ Bons (15-25KB): {good}")
print(f"  ⚠️ Incompletos (5-15KB): {incomplete}")
print(f"  ❌ Vazios (<5KB): {empty}")
print(f"  ❌ Corrompidos: {corrupted}")
print(f"  ❌ Não encontrados: {not_found}")
print()

# Estatísticas de conteúdo
total_exercises = sum(r.get('exercises', 0) for r in results)
with_examples = sum(1 for r in results if r.get('has_examples', False))
with_formulas = sum(1 for r in results if r.get('has_formulas', False))
with_charts = sum(1 for r in results if r.get('charts', 0) > 0)

print("📝 Conteúdo:")
print(f"  Total de exercícios: {total_exercises}")
print(f"  Capítulos com exemplos: {with_examples}/{total}")
print(f"  Capítulos com fórmulas: {with_formulas}/{total}")
print(f"  Capítulos com gráficos: {with_charts}/{total}")
print()

# Detalhamento por status
print("=" * 80)
print("📋 DETALHAMENTO POR CATEGORIA")
print("=" * 80)
print()

if complete > 0:
    print(f"✅ CAPÍTULOS COMPLETOS ({complete}):")
    for r in results:
        if r.get('status') == 'COMPLETE':
            print(f"   • Cap {r['number']}: {r['title']} ({r['size']/1024:.1f}KB, {r['exercises']} ex)")
    print()

if good > 0:
    print(f"✅ CAPÍTULOS BONS ({good}):")
    for r in results:
        if r.get('status') == 'GOOD':
            print(f"   • Cap {r['number']}: {r['title']} ({r['size']/1024:.1f}KB, {r['exercises']} ex)")
    print()

if incomplete > 0:
    print(f"⚠️ CAPÍTULOS INCOMPLETOS ({incomplete}):")
    for r in results:
        if r.get('status') == 'INCOMPLETE':
            print(f"   • Cap {r['number']}: {r['title']} ({r['size']/1024:.1f}KB)")
    print()

if empty > 0:
    print(f"❌ CAPÍTULOS VAZIOS/BÁSICOS ({empty}):")
    for r in results:
        if r.get('status') == 'EMPTY':
            print(f"   • Cap {r['number']}: {r['title']} ({r['size']/1024:.1f}KB)")
    print()

if corrupted > 0:
    print(f"❌ CAPÍTULOS CORROMPIDOS ({corrupted}):")
    for r in results:
        if r.get('status') == 'CORRUPTED':
            print(f"   • Cap {r['number']}: {r['title']}")
    print()

# Recomendações
print("=" * 80)
print("💡 RECOMENDAÇÕES")
print("=" * 80)
print()

if empty + incomplete > 0:
    print(f"⚠️ {empty + incomplete} capítulos precisam de conteúdo completo")
    print("   Recomendação: Recriar com conteúdo detalhado")
    print()

if with_charts < 3:
    print(f"📊 Apenas {with_charts}/10 capítulos têm gráficos")
    print("   Recomendação: Adicionar visualizações nos capítulos prioritários")
    print()

if complete + good >= 7:
    print(f"🎉 {complete + good} capítulos estão em bom estado!")
    print("   Foco: Completar os capítulos restantes")
    print()

print("=" * 80)
print("✅ REVISÃO CONCLUÍDA")
print("=" * 80)
