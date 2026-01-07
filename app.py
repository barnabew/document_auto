import streamlit as st
from generate_documents import generate_document

st.set_page_config(page_title="Document Generator", layout="wide")



document_type = st.sidebar.selectbox(
    "Select Document Type",
    ["contract", "invoice", "report"]
)

st.subheader(f"Generate {document_type.capitalize()}")

with st.form("document_form"):
    data = {}

    if document_type == "contract":
            data["ClientName"] = st.text_input("Client Name")
            data["Address"] = st.text_input("Address")
            data["StartDate"] = st.text_input("Start Date (YYYY-MM-DD)")
            data["EndDate"] = st.text_input("End Date (YYYY-MM-DD)")
            data["Amount"] = st.number_input("Amount (€)", min_value=0.0)
            data["Subject"] = st.text_input("Subject")
    elif document_type == "invoice":
            data["ClientNname"] = st.text_input("Client Name")
            data["Address"] = st.text_input("Address")
            data["InvoiceDate"] = st.text_input("Invoice Date (YYYY-MM-DD)")
            data["InvoiceNumber"] = st.text_input("Invoice Number")
            data["Amount"] = st.number_input("Amount (€)", min_value=0.0)
            data["Description"] = st.text_input("Description")
    elif document_type == "report":
            data["Start_date"] = st.text_input("Start Date (YYYY-MM-DD)")
            data["EndDate"] = st.text_input("End Date (YYYY-MM-DD)")
            data["KPI1"] = st.number_input("KPI1 (€)", min_value=0.0)
            data["KPI1"] = st.number_input("KPI2")
            data["KPI1"] = st.number_input("KPI3 (%)", min_value=0.0)
            data["Summary"] = st.text_area("Summary")
            
    
    submitted = st.form_submit_button("Generate Document")


if submitted:
    output_path = generate_document(document_type, data)
    st.success("Document generated successfully!")
    st.download_button(
        "Download PDF",
        open(output_path, "rb"),
        file_name=output_path.name

    )



