import fitz  # PyMuPDF

def extract_text_blocks(pdf_path):
    doc = fitz.open(pdf_path)
    blocks = []

    for page_num, page in enumerate(doc):
        try:
            text_blocks = page.get_text("dict")["blocks"]
            for block in text_blocks:
                if "lines" not in block:
                    continue
                for line in block["lines"]:
                    for span in line["spans"]:
                        if span["text"].strip():
                            blocks.append({
                                "text": span["text"].strip(),
                                "font_size": span["size"],
                                "page": page_num + 1
                            })
        except Exception as e:
            print(f"[PyMuPDF Error] Page {page_num + 1}: {e}")
    
    return blocks
