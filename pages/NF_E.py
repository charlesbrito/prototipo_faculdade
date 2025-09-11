import streamlit as st
from datetime import date
from fpdf import FPDF
from io import BytesIO
import base64


def nfe():
    st.title("Gere sua nota fiscal")
    if 'nfe' not in st.session_state:
        st.session_state.nfe = []

    with st.form("nfe-form"):
        st.subheader("Informações do cliente")
        nome = st.text_input("Nome do cliente")
        cpf_cnpj = st.text_input("CPF ou CNPJ do cliente")
        endereco = st.text_input("Endereço do cliente")
       
        st.subheader("informações do produto")
        produto = st.text_input("Produto")
        st.subheader("Totais")
        valor_produto = st.text_input("Valores do produto")
        impostos = st.text_input("Valores de impostos")
        valor_final = st.text_input("Valor final")
        
        st.subheader("Forma de pagamento")
        forma_pagamento = st.text_input("Forma de pagamento")

        gerar = st.form_submit_button("Gerar Nota Fiscal")

        if gerar:
            
            dados = {
                "Nome": nome,
                "CPF/CNPJ": cpf_cnpj,
                "Endereço": endereco,
                "Produto": produto,
                "Valor do produto": valor_produto,
                "Impostos": impostos,
                "Valor final": valor_final,
                "Forma de pagamento": forma_pagamento
            }

            pdf = FPDF()
            pdf.add_page()

            # Cabeçalho
            pdf.set_font("Arial", "B", 16)
            pdf.cell(0, 10, "Relatório de Cadastro", ln=True, align="C")
            pdf.ln(10)

            # Dados do formulário
            pdf.set_font("Arial", size=12)
            for campo, valor in dados.items():
                pdf.multi_cell(0, 8, f"{campo}: {valor}")
                pdf.ln(2)

            # Rodapé
            pdf.set_y(-20)
            pdf.set_font("Arial", "I", 8)
            pdf.cell(0, 10, "Gerado pelo sistema Streamlit", align="C")

            # Retornar PDF em bytes
            pdf_bytes = pdf.output(dest='S').encode('latin-1')
            b64_pdf = BytesIO(pdf_bytes)

            st.session_state['pdf_buffer'] = b64_pdf


if 'pdf_buffer' in st.session_state:
    st.download_button(
        label="📥 Baixar PDF",
        data=st.session_state['pdf_buffer'],
        file_name=f"nota_fiscal.pdf",
        mime="application/pdf"
    )
                
        
            
       
    






if __name__ == '__main__':
    nfe()
