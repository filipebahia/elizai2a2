import streamlit as st
import openai
from PIL import Image

left_co, cent_co,last_co = st.columns(3)
with last_co:
    logo_i2a2 = Image.open('logo.png')
    st.image(logo_i2a2, width = 150)

with left_co:
    st.title("ChatENT")

st.write("????ChatENT, Eliza New Times. A mais recente inovação em assistência terapêutica. Inspirada na icônica Eliza, esta nova ferramenta com tecnologia de ponta é mais inteligente e empática, com uma nova abordagem para apoiar questões emocionais, além de proporcionar privacidade garantida. Descubra uma nova forma de autocuidado e bem-estar emocional.")

# Instruções
with st.expander("Instruções", expanded = True):
    st.write("- bla\n"
             "- bla bla\n"
             "- bla bla bla\n"
             "- bla bla bla bla\n"
             "- bla bla bla bla bla\n"
             "- bla bla bla bla bla bla")

#formAPI = st.empty()

with st.expander("API Key"):
    with st.form(key='api_key', clear_on_submit=True): # Limpa somente o texto inserido
        #col1, col2 = st.columns(2)
        #apiKey = col1.text_input('API key', type = "password") # Sem colunas substituir col1.text_input por st.text_input
        #enviarKey = col2.form_submit_button(label="Enviar API KEY") # Sem colunas substituir col2.form_submit_button por st.form_submit_button
        apiKey = st.text_input('Insira sua chave:')#, type = "password")
        enviarKey = st.form_submit_button(label="Confirmar")

global tempKey

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

try:
    if message := st.chat_input("Como posso te ajudar?"):
        openai.api_key = apiKey
        st.chat_message("user").markdown(message)
        st.session_state.messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model = "gpt-3.5-turbo", messages = st.session_state.messages, temperature = 0.5, max_tokens = 1000)
        reply = chat.choices[0].message.content
        #response = f"Echo: {reply}"
        response = reply
        with st.chat_message("assistant"):
            st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
        openai.api_key = "0"

except Exception:
    st.error('Insira sua API Key. Caso tenha inserido, verifique se a chave está correta!', icon="🚨")
#    #st.write("Insira sua API Key. Caso tenha inserido, por favor verifique se a chave está correta!")

if enviarKey:
    tempKey = apiKey
    openai.api_key = tempKey
    st.session_state.messages = [{"role": "system", "content": "Converse somente sobre terapia. Imagine estar conversando com alguém que esteja precisando de uma terapia. Se o assunto desviar disto, pode encerrar a conversa"}]
    #st.session_state.messages = [{"role": "system", "content": "Este chat é de uso exclusivo para atendimento terapêutico. Evite conversar sobre temas que não estejam relacionados com terapia."}]
    #st.session_state.messages = [{"role": "system", "content": "Assistente exclusiva de terapia"}]
    #teste.empty()
    st.success("API Key informada com sucesso!")



