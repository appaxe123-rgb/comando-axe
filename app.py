import streamlit as st

# Configuração da Página para bloquear prints simples via layout
st.set_page_config(page_title="Comando Axé", layout="centered")

# Estilo CSS para dificultar cópias e esconder elementos se necessário
st.markdown("""
    <style>
    @media print {
        body { display: none !important; }
    }
    .stApp {
        -webkit-touch-callout: none;
        -webkit-user-select: none;
        -khtml-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Comando Axé")
st.info("🔒 Este sistema utiliza proteção avançada de dados e acesso restrito.")

# Sistema de Login Simples
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    with st.form("login"):
        user = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        if st.form_submit_button("Acessar"):
            if user == "admin" and senha == "axe2026": # Exemplo de senha
                st.session_state.autenticado = True
                st.rerun()
            else:
                st.error("Acesso negado. Verifique suas credenciais.")
else:
    st.success("Bem-vindo ao Comando Axé")
    st.write("O conteúdo está protegido contra capturas de tela.")
    if st.button("Sair"):
        st.session_state.autenticado = False
        st.rerun()
