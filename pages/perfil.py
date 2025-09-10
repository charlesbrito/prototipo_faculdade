import streamlit as st

def perfil():
    st.title("Veja seu perfil")
    st.image("logo_empresa.jpeg", width=150)

    empresa = {
        "Nome": "SoluTec",
        "CNPJ": "12.345.678/0001-90",
        "Endereço": "Avenida Getúlio Vargas",
        "Telefone": "(73) 9 99845-5466",
        "Setor":"Tecnologia da informação",
        "Responsável":"Open source"
    }

    for k, v in empresa.items():
        st.write(f"**{k}: **{v}")


if __name__ == '__main__':
    perfil()