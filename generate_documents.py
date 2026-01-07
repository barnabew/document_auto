import uuid
from docxtpl import DocxTemplate
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


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




def generate_document(template_path, data):

    template_path = Path(template_path) 
    template = DocxTemplate(template_path)

    # Crée un dossier output s'il n'existe pas
    output_dir = BASE_DIR / "output"
    output_dir.mkdir(exist_ok=True)

    # Nom unique pour éviter les collisions
    unique_id = uuid.uuid4().hex[:8]
    docx_file = output_dir / f"{template_path.stem}_{unique_id}.docx"

    # Remplit les placeholders
    template.render(data)
    template.save(docx_file)

    return docx_file
