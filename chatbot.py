import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

#CONFIGURATION PAGE
st.set_page_config(page_title="Chatbot IA", page_icon="🤖")

st.title("💬 Chatbot")

#INITIALISATION
if "history" not in st.session_state:
    st.session_state.history = {"user": [], "assistant": []}

# Initialiser LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)

#AFFICHER L'HISTORIQUE
for u_msg, a_msg in zip(st.session_state.history["user"], st.session_state.history["assistant"]):
    with st.chat_message("user"):
        st.markdown(u_msg)
    with st.chat_message("assistant"):
        st.markdown(a_msg)

#ENTRÉE UTILISATEUR
if prompt := st.chat_input("Votre message..."):
    # Ajouter le message utilisateur
    st.session_state.history["user"].append(prompt)
    with st.chat_message("user"):
        st.markdown(prompt)

    # Construire un contexte en français
    context = ""
    for u, a in zip(st.session_state.history["user"], st.session_state.history["assistant"]):
        context += f"Utilisateur: {u}\nAssistant: {a}\n"
    context += f"Utilisateur: {prompt}\nAssistant:"

    # Obtenir la réponse
    response = llm.invoke(context).content

    # Ajouter la réponse de l’IA
    st.session_state.history["assistant"].append(response)
    with st.chat_message("assistant"):
        st.markdown(response)

#BOUTON RESET - pour réinitialiser
if st.button("🔄 Réinitialiser la conversation"):
    st.session_state.history = {"user": [], "assistant": []}
    st.success("La conversation a été réinitialisée ✅")
    st.rerun() 
