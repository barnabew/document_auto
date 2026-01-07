import uuid
from docxtpl import DocxTemplate
from pathlib import Path
from docx2pdf import convert

BASE_DIR = Path(__file__).resolve().parent.parent # Adjusted to go up one level


CONFIG = {
    "contract": {
        "template": BASE_DIR / "templates" / "contract_template.docx",
        "output_prefix": "contract"
    },
    "invoice": {
        "template": BASE_DIR / "templates" / "invoice_template.docx",
        "output_prefix": "invoice"
    },
    "report": {
        "template": BASE_DIR / "templates" / "report_template.docx",
        "output_prefix": "report"
    }
}



def generate_document(document_type, data):
    
    config = CONFIG[document_type]


    template_path= config["template"]
    output_prefix = config["output_prefix"] 

    template = DocxTemplate(template_path)

    output_dir = BASE_DIR / "output"
    output_dir.mkdir(exist_ok=True)

    unique_id = uuid.uuid4().hex[:8]

    docx_file = output_dir / f"{output_prefix}_{unique_id}.docx"
    pdf_file = output_dir / f"{output_prefix}_{unique_id}.pdf"

    template = DocxTemplate(template_path)
    template.render(data)
    template.save(docx_file)

    # Conversion PDF
    convert(docx_file, pdf_file)

    # Supprimer le DOCX (optionnel mais recommandé)
    docx_file.unlink()

    return pdf_file
