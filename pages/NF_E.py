import streamlit as st
from datetime import date
from weasyprint import HTML
import base64
from io import BytesIO

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
            html_content = f"""
            <html>
                <head>
                    <title>Relatório de Cadastro</title>
                    <style>
                        body {{
                            font-family: Arial, sans-serif;
                            margin: 20px;
                        }}
                        h1 {{
                            color: #4CAF50;
                        }}
                        .campo {{
                            margin-bottom: 10px;
                        }}
                        .campo b {{
                            color: #333;
                        }}
                    </style>
                </head>
                <body>
                    <h1>Relatório de Cadastro</h1>
                    <div class="campo"><b>Nome:</b> {nome}</div>
                    <div class="campo"><b>CPF/CNPJ:</b> {cpf_cnpj}</div>
                    <div class="campo"><b>Endereço:</b> {endereco}</div>
                    <div class="campo"><b>Produto:</b> {produto}</div>
                    <div class="campo"><b>Valor do produto:</b> {valor_produto}</div>
                    <div class="campo"><b>Impostos:</b> {impostos}</div>
                    <div class="campo"><b>Valor final:</b> {valor_final}</div>
                    <div class="campo"><b>Forma de pagamento:</b> {forma_pagamento}</div>
                </body>
            </html>
            """

            # Gerando o PDF
            pdf = HTML(string=html_content).write_pdf()

            # Criando o link de download
            pdf_bytes = BytesIO(pdf)
            pdf_bytes.seek(0)
            b64_pdf = base64.b64encode(pdf_bytes.read()).decode()

            href = f'<a href="data:application/octet-stream;base64,{b64_pdf}" download="nota_fiscal_{nome}.pdf">Clique aqui para baixar o PDF</a>'
            st.markdown(href, unsafe_allow_html=True)

            
       
            
       
    






if __name__ == '__main__':
    nfe()
