import os
import json
from extractor import extract_text_blocks
from refiner import refine_headings

INPUT_DIR = '/app/input'
OUTPUT_DIR = '/app/output'

def process_pdf(pdf_path, output_path):
    blocks = extract_text_blocks(pdf_path)
    title, outline = refine_headings(blocks)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump({
            "title": title,
            "outline": outline
        }, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith('.pdf'):
            input_path = os.path.join(INPUT_DIR, filename)
            output_filename = os.path.splitext(filename)[0] + '.json'
            output_path = os.path.join(OUTPUT_DIR, output_filename)
            print(f"Processing: {filename}")
            process_pdf(input_path, output_path)
