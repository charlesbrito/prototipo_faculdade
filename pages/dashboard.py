import streamlit as st
import pandas as pd
import random 

def dashboard():
    st.title("Dashboard")
    meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"]

    receita = [random.randint(3000, 7000) for _ in range(12)]
    despesas = [random.randint(1500, 4000) for _ in range (12)]
    lucro = [r-d for r,d in zip(receita,despesas)]
    clientes = [random.randint(15, 60) for _ in range(12)]

    vendas_produtos = {
        "Produto A": random.randint(5000, 15000),
        "Produto B": random.randint(3000, 12000),
        "Produto C ": random.randint(1000,8000)
    }

    df = pd.DataFrame({
        "Mês": meses,
        "Receitas": receita,
        "Despesas": despesas,
        "Lucro": lucro,
        "Clientes": clientes
    })

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Receita, Despesas e Lucro")
        st.line_chart(df.set_index("Mês")[["Receitas","Despesas","Lucro"]])

    with col2:
        st.subheader("Clientes por mês")
        st.bar_chart(df.set_index("Mês")["Clientes"])

    # Gráfico de pizza abaixo das colunas
    st.subheader("Vendas por produto")
    vendas_produto_df = pd.DataFrame.from_dict(vendas_produtos, orient="index", columns=["Valor"])
    st.pyplot(vendas_produto_df.plot.pie(y="Valor", autopct="%1.1f%%", legend=False, figsize=(5,5)).figure)

if __name__ == "__main__":
    dashboard()