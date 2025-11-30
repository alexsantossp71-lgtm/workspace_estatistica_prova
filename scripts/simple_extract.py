import json
from pypdf import PdfReader

# Read PDF
reader = PdfReader('Estat_stica_Aplicada_6_Edi_o_Faber_e_Lar.pdf')

# Extract Chapter 1 (pages approximately 2-40)
chapter1_text = ""
for i in range(2, 40):
    chapter1_text += reader.pages[i].extract_text() + "\n"

# Extract Chapter 2 (pages approximately 40-80)
chapter2_text = ""
for i in range(40, 80):
    chapter2_text += reader.pages[i].extract_text() + "\n"

# Save to text files for review
with open('chapter1_raw.txt', 'w', encoding='utf-8') as f:
    f.write(chapter1_text)

with open('chapter2_raw.txt', 'w', encoding='utf-8') as f:
    f.write(chapter2_text)

print("Extracted Chapter 1 length:", len(chapter1_text))
print("Extracted Chapter 2 length:", len(chapter2_text))
print("\nFirst 500 chars of Chapter 1:")
print(chapter1_text[:500])
print("\nFirst 500 chars of Chapter 2:")
print(chapter2_text[:500])
