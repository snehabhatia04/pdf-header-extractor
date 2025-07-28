# PDF Heading Extractor

A Dockerized solution that extracts the title and hierarchical headings (H1, H2, H3) from PDFs. Designed for offline execution under 10 seconds with a model size under 200MB. Supports fallback OCR (English & Japanese) for scanned or image-based PDFs.

---

## 🔧 Approach

1. **Text Extraction**:
   - Uses **PyMuPDF (fitz)** for fast, layout-preserving PDF text block extraction.
   - Falls back to **Tesseract OCR** for scanned/image-based pages or when PyMuPDF fails.

2. **Heading Detection**:
   - Dynamically detects heading levels (H1, H2, H3) using layout features like font size, boldness, and relative position on page.
   - Handles irregular formats without relying solely on font size.

3. **OCR Support**:
   - Integrated with **Tesseract (English + Japanese)** for multilingual handling.
   - Automatically detects when to switch to OCR based on PyMuPDF fallback.

---

## 📁 Expected Input/Output

- **Input**: PDF files in `/app/input`
- **Output**: Structured `filename.json` for each `filename.pdf` in `/app/output`

### Sample Output Format

```json
[
  {
    "level": "title",
    "text": "Document Title",
    "page": 1
  },
  {
    "level": "H1",
    "text": "Section One",
    "page": 1
  },
  {
    "level": "H2",
    "text": "Subsection One-One",
    "page": 2
  }
]


## How to Build & Run

container must not require internet access and should run within 10 seconds for a 50-page PDF.

### Build

```bash
docker build --platform linux/amd64 -t heading-extractor:<identifier> .


## Run Instructions

### Run (Linux/macOS)

```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none heading-extractor:<identifier>


### Run (Windows CMD)
```bash
docker run --rm -v %cd%/input:/app/input -v %cd%/output:/app/output --network none heading-extractor:<identifier>


## Dependencies
All dependencies are installed within the Docker image:

Python 3.10 (Alpine base)

PyMuPDF (fitz)