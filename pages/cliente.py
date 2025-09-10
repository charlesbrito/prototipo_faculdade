import streamlit as st
import pandas as pd

def cliente():
    st.title("Cadastre aqui seus clientes")
    if 'clientes' not in st.session_state:
        st.session_state.clientes = []
    with st.form('form_cliente'):
        n_cliente = st.text_input("Nome do cliente")
        endereco = st.text_input("Endereço")
        telefone = st.text_input("Telefone")
        email = st.text_input("Email")

        cadastrar = st.form_submit_button("Registrar cliente")

        if cadastrar:
            st.session_state.clientes.append({
                "Nome do cliente": n_cliente,
                "Endereço": endereco,
                "Telefone": telefone,
                "Email": email
            })
            st.success("Cliente cadastrado com sucesso")
    if st.session_state.clientes:
        st.subheader("Lista de clientes")
        df = pd.DataFrame(st.session_state.clientes)
        st.dataframe(df, use_container_width=True)

    



if __name__ == '__main__':
    cliente()