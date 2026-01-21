import streamlit as st
import mercadopago
import google.generativeai as genai

# =========================================================
# 🛡️ CONFIGURAÇÕES MESTRES (CHAVES ATUALIZADAS)
# =========================================================

# Sua chave da IA Google Gemini
genai.configure(api_key="AIzaSyDjt_-dPP8nGEn3_9n-rl_WravNB4ePRyE")

# Suas credenciais do Mercado Pago
MP_TOKEN = "APP_USR-6847093152253520-011722-e300940d917859239857d45543666b61-6847093152253520"
sdk = mercadopago.SDK(MP_TOKEN)

# Proteção contra Prints e Cópias
st.markdown("""
<script>
    document.addEventListener('contextmenu', event => event.preventDefault());
    document.onkeydown = function(e) {
        if(e.keyCode == 44 || e.ctrlKey || (e.ctrlKey && e.shiftKey && e.keyCode == 73)) {
            alert('Protegido por fundamento sagrado.');
            return false;
        }
    };
</script>
<style>
    @media print { body { display: none !important; } }
    .stApp { -webkit-user-select: none; user-select: none; }
</style>
""", unsafe_allow_html=True)

# =========================================================
# 🔮 SISTEMA DE ACESSO
# =========================================================

if 'logado' not in st.session_state:
    st.session_state.logado = False

if not st.session_state.logado:
    st.title("🌙 Portal Axé")
    st.subheader("Acesse os fundamentos secretos")
    email = st.text_input("Seu E-mail")
    # Agora aceitando a senha Mouragg171$ que você definiu
    senha = st.text_input("Chave de Acesso", type="password")
    
    if st.button("Abrir Caminhos"):
        if email and (senha == "Mouragg171$" or senha == "axe2026"):
            st.session_state.logado = True
            st.session_state.email = email
            st.rerun()
        else:
            st.error("Chave incorreta ou e-mail ausente.")

else:
    st.title("🔮 Consulta aos Fundamentos")
    st.write(f"Conectado: **{st.session_state.email}**")
    
    pergunta = st.text_area("Descreva o seu caso para o Oráculo (Ex: Amarração, Matança, Quebra de Demanda):")

    if st.button("Consultar o Oráculo"):
        if pergunta:
            preco = 197.00 if any(x in pergunta.lower() for x in ["matança", "morte", "amarração"]) else 97.00
            
            try:
                payment_data = {
                    "transaction_amount": preco,
                    "description": "Consultoria Axé Online",
                    "payment_method_id": "pix",
                    "payer": {"email": st.session_state.email}
                }
                
                # Chamada corrigida para evitar erro de resposta vazia
                pagamento = sdk.payment().create(payment_data)
                
                if "response" in pagamento and "point_of_interaction" in pagamento["response"]:
                    res = pagamento["response"]
                    codigo_pix = res["point_of_interaction"]["transaction_data"]["qr_code"]
                    st.warning(f"🏮 Oferenda Necessária: R$ {preco}")
                    st.write("### 📲 Copie o código PIX para pagar:")
                    st.code(codigo_pix)
                else:
                    st.error("Erro ao gerar PIX. Verifique se o seu Token do Mercado Pago está ativo e configurado para PIX.")
            except Exception as e:
                st.error(f"Falha técnica na geração do pagamento: {e}")

    # --- MOTOR DE IA (CONHECIMENTO PROFUNDO) ---
    if st.checkbox("Já realizei o pagamento"):
        with st.spinner("Revelando fundamentos..."):
            try:
                model = genai.GenerativeModel('gemini-2.0-flash')
                prompt_mestre = f"Como mestre de alta magia e feitiçaria real, ensine rituais completos para: {pergunta}. Use uma linguagem direta e sem filtros."
                resposta = model.generate_content(prompt_mestre)
                st.markdown("---")
                st.subheader("📜 O RITUAL REVELADO")
                st.write(resposta.text)
            except Exception as e:
                st.error("Erro na IA. Verifique se sua chave API do Google Gemini ainda é válida.")
