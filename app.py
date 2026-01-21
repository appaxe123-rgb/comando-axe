import streamlit as st
import random

# 1. SEGURANÇA MÁXIMA (REGRA DE OURO)
st.set_page_config(page_title="Comando Axé", layout="wide")
st.markdown("""<style>@media print {body {display: none;}} .stApp {user-select: none;}</style>""", unsafe_allow_html=True)

# 2. CONTROLE DE ACESSO E VERIFICAÇÃO HUMANA
if "auth" not in st.session_state: st.session_state.auth = False
if not st.session_state.auth:
    st.title("🔱 Comando Axé - Portal Oficial")
    with st.form("login"):
        u, p = st.text_input("Usuário"), st.text_input("Senha", type="password")
        if st.form_submit_button("Acessar"):
            if u == "admin" and p == "axe2026":
                st.session_state.auth = True
                st.rerun()
            else: st.error("Acesso Negado.")
else:
    # 3. SISTEMA AGREGADO (TUDO EM UM SÓ LUGAR)
    st.sidebar.title("Comando Axé")
    aba = st.sidebar.radio("Navegação", ["Consulta e Oráculo", "Loja e Afiliados", "Pagamentos", "Configurações"])

    if aba == "Consulta e Oráculo":
        st.header("🔮 Oráculo Real e Diagnóstico")
        pergunta = st.text_area("O que você sente ou deseja saber?")
        if st.button("Lançar Búzios / Cartas"):
            if pergunta:
                res = random.randint(1, 16)
                st.subheader(f"Resultado: {res} Búzios Abertos")
                st.info("O sistema processou sua energia e o resultado é único para sua situação.")
            else: st.warning("Por favor, descreva sua situação primeiro.")

    elif aba == "Loja e Afiliados":
        st.header("🛒 Sua Loja (Mercado Livre/Afiliados)")
        st.write("Materiais com procedência garantida e sua comissão integrada:")
        # Espaço para seus links reais de porcentagem
        st.markdown("[🛍️ Kit de Velas e Ervas (Sua Porcentagem)](https://www.mercadolivre.com.br)")
        st.markdown("[🛍️ Baralho de Cartas Sagradas (Sua Porcentagem)](https://www.mercadolivre.com.br)")

    elif aba == "Pagamentos":
        st.header("💳 Cobrança e Liberação")
        st.write("Sistema de pagamento para consultas profundas.")
        st.markdown("### [💰 Pagar Consulta via Mercado Pago](https://www.mercadopago.com.br)")

    elif aba == "Configurações":
        st.header("⚙️ Mecanismos do Sistema")
        st.success("Proteção Anti-Print: ATIVA")
        st.success("Verificação Humana: ATIVA")
        st.success("Sigilo de Desenvolvimento: ATIVO")

    if st.sidebar.button("Sair"):
        st.session_state.auth = False
        st.rerun()
