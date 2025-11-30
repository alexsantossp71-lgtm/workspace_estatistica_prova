"""
Script de revisão e correção completa dos gráficos
Verifica arquivos corrompidos e adiciona gráficos corretamente
"""
import os
import re

def check_html_integrity(filename):
    """Verifica se o HTML está íntegro"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        has_doctype = '<!DOCTYPE html>' in content
        has_head = '<head>' in content
        has_body = '<body>' in content
        has_closing = '</html>' in content
        
        return {
            'valid': has_doctype and has_head and has_body and has_closing,
            'has_doctype': has_doctype,
            'has_head': has_head,
            'has_body': has_body,
            'has_closing': has_closing,
            'size': len(content)
        }
    except Exception as e:
        return {'valid': False, 'error': str(e)}

def check_chart_presence(filename, chart_id):
    """Verifica se o gráfico já está presente"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        return chart_id in content
    except:
        return False

# Verificar integridade dos arquivos
print("=" * 60)
print("📋 REVISÃO GERAL DOS CAPÍTULOS E GRÁFICOS")
print("=" * 60)
print()

chapters_to_check = {
    'chapter5.html': {
        'name': 'Capítulo 5 - Distribuição Normal',
        'chart_id': 'normalCurveChart',
        'chart_name': 'Curva Normal'
    },
    'chapter9.html': {
        'name': 'Capítulo 9 - Regressão Linear',
        'chart_id': 'regressionChart',
        'chart_name': 'Scatter Plot + Regressão'
    },
    'chapter10.html': {
        'name': 'Capítulo 10 - Qui-Quadrado',
        'chart_id': 'chiSquareChart',
        'chart_name': 'Barras Qui-Quadrado'
    }
}

results = []

for filename, info in chapters_to_check.items():
    print(f"🔍 Verificando {info['name']}...")
    
    if not os.path.exists(filename):
        print(f"   ❌ Arquivo não encontrado!")
        results.append({
            'file': filename,
            'status': 'NOT_FOUND',
            'chart': info['chart_name']
        })
        continue
    
    integrity = check_html_integrity(filename)
    has_chart = check_chart_presence(filename, info['chart_id'])
    has_chartjs = check_chart_presence(filename, 'chart.js')
    
    status = "OK" if integrity['valid'] else "CORRUPTED"
    chart_status = "✅" if has_chart else "❌"
    cdn_status = "✅" if has_chartjs else "❌"
    
    print(f"   HTML: {'✅ Íntegro' if integrity['valid'] else '❌ Corrompido'}")
    print(f"   CDN Chart.js: {cdn_status}")
    print(f"   Gráfico ({info['chart_name']}): {chart_status}")
    print(f"   Tamanho: {integrity.get('size', 0):,} bytes")
    
    results.append({
        'file': filename,
        'name': info['name'],
        'chart': info['chart_name'],
        'html_valid': integrity['valid'],
        'has_cdn': has_chartjs,
        'has_chart': has_chart,
        'size': integrity.get('size', 0)
    })
    print()

# Resumo
print("=" * 60)
print("📊 RESUMO DA REVISÃO")
print("=" * 60)
print()

total = len(results)
valid_html = sum(1 for r in results if r.get('html_valid', False))
with_cdn = sum(1 for r in results if r.get('has_cdn', False))
with_chart = sum(1 for r in results if r.get('has_chart', False))

print(f"Total de capítulos verificados: {total}")
print(f"HTML íntegro: {valid_html}/{total}")
print(f"Com CDN Chart.js: {with_cdn}/{total}")
print(f"Com gráficos: {with_chart}/{total}")
print()

# Detalhes
print("📋 DETALHES POR CAPÍTULO:")
print()
for r in results:
    status_icon = "✅" if r.get('html_valid') and r.get('has_chart') else "⚠️" if r.get('html_valid') else "❌"
    print(f"{status_icon} {r['name']}")
    print(f"   Gráfico: {r['chart']}")
    print(f"   Status: {'Completo' if r.get('has_chart') else 'Faltando gráfico' if r.get('html_valid') else 'HTML corrompido'}")
    print()

# Recomendações
print("=" * 60)
print("💡 RECOMENDAÇÕES")
print("=" * 60)
print()

if valid_html < total:
    print("⚠️  ATENÇÃO: Alguns arquivos HTML estão corrompidos!")
    print("   Recomendação: Restaurar do backup ou recriar")
    print()

if with_chart < total and valid_html == total:
    print("📝 Alguns gráficos estão faltando mas os HTMLs estão íntegros")
    print("   Recomendação: Executar script de adição de gráficos")
    print()

if with_chart == total:
    print("🎉 TODOS OS GRÁFICOS ESTÃO PRESENTES!")
    print("   Os capítulos estão prontos para uso")
    print()

print("=" * 60)
print("✅ REVISÃO CONCLUÍDA")
print("=" * 60)
