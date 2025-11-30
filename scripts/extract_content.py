import os
import json
import re
import requests
from pypdf import PdfReader

# Configuration
PDF_PATH = "Estat_stica_Aplicada_6_Edi_o_Faber_e_Lar.pdf"
OUTPUT_DIR = "src/data"
OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3:8b"

def extract_text_from_pdf(pdf_path):
    print(f"Loading PDF: {pdf_path}")
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

def split_into_chapters(text):
    # Heuristic: Split by "Capítulo X" or "CAPÍTULO X"
    pattern = r"(Capítulo\s+\d+|CAPÍTULO\s+\d+)"
    parts = re.split(pattern, text)
    
    chapters = []
    
    # Iterate over the split parts.
    for i in range(1, len(parts), 2):
        title = parts[i].strip()
        content = parts[i+1] if i+1 < len(parts) else ""
        
        # Normalize title to check for Chapter 1 and 2
        # We only want "Capítulo 1" and "Capítulo 2" (ignoring sub-sections if any, though regex captures just the header)
        # Let's be strict: check if the number is 1 or 2.
        match = re.search(r"\d+", title)
        if match:
            num = int(match.group(0))
            if num in [1, 2]:
                chapters.append({"title": title, "content": content, "number": num})
        
    return chapters

def summarize_with_ollama(text, title):
    print(f"Summarizing: {title}...")
    truncated_text = text[:25000] # Increased to capture more content
    
    prompt = f"""
    Você é um assistente especialista em estatística e design educacional.
    Analise o seguinte conteúdo do capítulo "{title}" de um livro de estatística.
    
    Seu objetivo é extrair e estruturar TODO o conteúdo relevante para estudo.
    
    Gere um JSON com a seguinte estrutura:
    {{
        "title": "{title}",
        "summary": "Um resumo conciso do capítulo.",
        "introduction": "Uma introdução detalhada ao tema do capítulo.",
        "sections": [
            {{
                "title": "Título da Seção (ex: Tipos de Dados)",
                "content": "Explicação detalhada e didática sobre o tópico, com exemplos se houver no texto."
            }}
        ],
        "keyPoints": ["Ponto chave 1", "Ponto chave 2", "Ponto chave 3", "Ponto chave 4"],
        "exercises": ["Questão 1 encontrada no texto", "Questão 2..."],
        "image_ideas": [
            {{
                "name": "concept_visualization",
                "description": "Uma descrição visual detalhada para gerar uma imagem que explique um conceito chave deste capítulo. Estilo moderno, educacional, 3D flat."
            }},
            {{
                "name": "real_world_example",
                "description": "Uma descrição visual para uma imagem que mostre uma aplicação no mundo real do tema do capítulo."
            }}
        ]
    }}
    
    Responda APENAS com o JSON válido. Certifique-se de que o JSON esteja bem formatado.
    
    Conteúdo:
    {truncated_text}
    """
    
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "format": "json"
    }
    
    try:
        response = requests.post(OLLAMA_API_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        return json.loads(result['response'])
    except Exception as e:
        print(f"Error summarizing {title}: {e}")
        return {
            "title": title,
            "summary": "Não foi possível gerar o resumo.",
            "keyPoints": [],
            "image_ideas": []
        }

def main():
    if not os.path.exists(PDF_PATH):
        print(f"PDF not found at {PDF_PATH}")
        return

    full_text = extract_text_from_pdf(PDF_PATH)
    target_chapters = split_into_chapters(full_text)
    
    if not target_chapters:
        print("No chapters 1 or 2 found.")
        return

    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    for chap in target_chapters:
        processed_data = summarize_with_ollama(chap['content'], chap['title'])
        print(f"Generated keys for {chap['title']}: {list(processed_data.keys())}")
        
        # Add metadata
        processed_data["chapter_number"] = chap["number"]
        
        filename = f"chapter_{chap['number']}.json"
        file_path = os.path.join(OUTPUT_DIR, filename)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(processed_data, f, ensure_ascii=False, indent=2)
            
        print(f"Saved {chap['title']} to {file_path}")

if __name__ == "__main__":
    main()
