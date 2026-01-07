import streamlit as st
import pandas as pd
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
            data["client_name"] = st.text_input("Client Name")
            data["address"] = st.text_input("Address")
            data["start_date"] = st.text_input("Start Date (YYYY-MM-DD)")
            data["end_date"] = st.text_input("End Date (YYYY-MM-DD)")
            data["amount"] = st.number_input("Amount (€)", min_value=0.0)
            data["subject"] = st.text_input("Subject")
    elif document_type == "invoice":
            data["client_name"] = st.text_input("Client Name")
            data["invoice_number"] = st.text_input("Invoice Number")
            data["date"] = st.text_input("Date (YYYY-MM-DD)")
            data["items"] = st.text_area("Items (one per line, format: description,quantity,price)")
            data["total_amount"] = st.number_input("Total Amount (€)", min_value=0.0)
    elif document_type == "report":
            data["report_title"] = st.text_input("Report Title")
            data["author"] = st.text_input("Author")
            data["date"] = st.text_input("Date (YYYY-MM-DD)")
            data["summary"] = st.text_area("Summary")
            data["conclusion"] = st.text_area("Conclusion")
    
    submitted = st.form_submit_button("Generate Document")


if submitted:
    output_path = generate_document(document_type, data)
    st.success("Document generated successfully!")
    st.download_button(
        "Download PDF",
        open(output_path, "rb"),
        file_name=output_path.name

    )

