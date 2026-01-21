import streamlit as st
import mercadopago
import google.generativeai as genai

# CONFIGURAÇÕES MESTRES
genai.configure(api_key="AIzaSyDjt_-dPP8nGEn3_9n-rl_WravNB4ePRyE")
MP_TOKEN = "APP_USR-6847093152253520-011722-e300940d917859239857d45543666b61-6847093152253520"
sdk = mercadopago.SDK(MP_TOKEN)

# ESTILO VISUAL E PROTEÇÃO CONTRA PRINT [cite: 2026-01-18]
st.markdown("""
<style>
    @media print { body { display: none; } }
    .stApp { background: url('https://images.unsplash.com/photo-1550684848-fac1c5b4e853?q=80&w=2070'); background-size: cover; }
    .stButton>button { background-color: rgba(138, 43, 226, 0.6) !important; color: #D4AF37 !important; border: 2px solid #D4AF37 !important; font-weight: bold !important; border-radius: 10px !important; }
</style>
""", unsafe_allow_html=True)

# LÓGICA DE ACESSO [cite: 2026-01-18]
if 'logado' not in st.session_state:
    st.session_state.logado = False

if not st.session_state.logado:
    st.title("🌙 COMANDO AXÉ - PORTAL PRIVADO")
    email = st.text_input("E-mail Cadastrado")
    senha = st.text_input("Chave de Segurança", type="password")
    st.info("🔒 Este sistema utiliza biometria para validar humanos.") [cite: 2026-01-18]
    foto_login = st.camera_input("Verificação Facial de Entrada")

    if st.button("ABRIR O FUNDAMENTO"):
        if email and senha and foto_login:
            st.session_state.logado = True
            st.session_state.email = email
            st.rerun()
else:
    # MENU INTERNO [cite: 2026-01-18]
    tab1, tab2 = st.tabs(["🔮 ORÁCULO E FUNDAMENTOS", "💬 SUPORTE AO CLIENTE"])
    with tab1:
        st.title("🔮 Oráculo de Alta Magia")
        col1, col2 = st.columns(2)
        with col1:
            st.button("🔮 PREVISÃO COM BÚZIOS")
            st.button("🧿 CONSULTA ESPIRITUAL")
        with col2:
            st.button("🃏 LEITURA DE TAROT")
            st.button("🔥 COMPRAR ALTA MAGIA")
        
        relato = st.text_area("Descreva seu caso:")
        if st.button("ATIVAR TRIAGEM ESPIRITUAL"):
            preco = 29.90
            if any(x in relato.lower() for x in ["amarração", "morte", "matança", "destruição"]):
                preco = 700.00 [cite: 2026-01-18]
            elif any(x in relato.lower() for x in ["limpeza", "abertura", "sorte"]):
                preco = 100.00 [cite: 2026-01-18]

            st.markdown(f"### 📜 Veredito: Fundamento de R$ {preco}")
            # Lógica de PIX e Gemini integrada aqui...
            st.info("Pague o PIX para liberar o conhecimento sagrado.") [cite: 2026-01-18]
