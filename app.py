import streamlit as st
from pathlib import Path
from docxtpl import DocxTemplate
from generate_documents import generate_document

st.set_page_config(page_title="Document Generator", layout="wide")



document_type = st.selectbox("Select Document Type",["Contract", "Invoice", "Report", "Custom Upload"])

st.write("Generate documents from templates. Use predefined types or upload your own template.")

data = {}

if document_type != "Custom Upload":
    with st.form("document_form"):
      
    
        if document_type == "Contract":
                data["ClientName"] = st.text_input("Client Name")
                data["Address"] = st.text_input("Address")
                data["StartDate"] = st.text_input("Start Date (YYYY-MM-DD)")
                data["EndDate"] = st.text_input("End Date (YYYY-MM-DD)")
                data["Amount"] = st.number_input("Amount (€)", min_value=0.0)
                data["Subject"] = st.text_input("Subject")
        elif document_type == "Invoice":
                data["ClientNname"] = st.text_input("Client Name")
                data["Address"] = st.text_input("Address")
                data["InvoiceDate"] = st.text_input("Invoice Date (YYYY-MM-DD)")
                data["InvoiceNumber"] = st.text_input("Invoice Number")
                data["Amount"] = st.number_input("Amount (€)", min_value=0.0)
                data["Description"] = st.text_input("Description")
        elif document_type == "Report":
                data["Start_date"] = st.text_input("Start Date (YYYY-MM-DD)")
                data["EndDate"] = st.text_input("End Date (YYYY-MM-DD)")
                data["KPI1"] = st.number_input("KPI1 (€)", min_value=0.0)
                data["KPI1"] = st.number_input("KPI2")
                data["KPI1"] = st.number_input("KPI3 (%)", min_value=0.0)
                data["Summary"] = st.text_area("Summary")
                
        
        submitted = st.form_submit_button("Generate Document")
    
    
    if submitted:
        template_path = Path(f"templates/{document_type.lower()}_template.docx")
        docx_file = generate_document(template_path, data)
        st.success(f"Document generated: {docx_file.name}")
        st.download_button("Download DOCX", open(docx_file, "rb"), file_name=docx_file.name)


else:
    uploaded_file = st.file_uploader("Upload your Word template (.docx)", type="docx")

    if uploaded_file:
        template_path = Path("templates") / uploaded_file.name
        with open(template_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        doc = DocxTemplate(template_path)
        placeholders = doc.get_undeclared_template_variables()

        with st.form("custom_form"):
            data = {}
            for field in placeholders:
                data[field] = st.text_input(field.replace("_", " ").title())
            
            submitted = st.form_submit_button("Generate Document")

        if submitted:
            docx_file = generate_document(template_path, data)
            st.success(f"Document generated: {docx_file.name}")
            st.download_button("Download DOCX", open(docx_file, "rb"), file_name=docx_file.name)






