import streamlit as st
import pandas as pd
from datetime import date

def receitas():
    st.title("Veja aqui suas receitas como registro de vendas e controle de recebimento ")
    if "vendas" not in st.session_state:
        st.session_state.vendas = []

    with st.form("form_venda"):
        co1, co2 = st.columns(2)
        with co1:
            cliente = st.text_input("Nome do cliente")
            produto = st.text_input("Nome do produto")
            quantidade = st.number_input("Quantidade", min_value=0, step=1)
        with co2:
            preco = st.number_input("Preço", min_value=0.0, step=0.1, format="%.2f")
            data_venda = st.date_input("Data da venda", value=date.today())

        submitted = st.form_submit_button("Registrar venda")

        if submitted:
            total = quantidade * preco
            st.session_state.vendas.append({
                "Cliente": cliente,
                "Produto": produto,
                "Quantidade": quantidade,
                "Preço unitário R$": preco,
                "Total R$": total,
                "Data": data_venda
            }
            )
            st.success(f"Venda registrada: {quantidade} x {produto} para {cliente} (R${total:.2f})")

    if st.session_state.vendas:
        st.subheader("Historico de vendas")
        df = pd.DataFrame(st.session_state.vendas)
        st.dataframe(df, use_container_width=True)

if __name__ == "__main__":
    receitas()