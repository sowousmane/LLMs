#LES IMPORTATIONS
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()


#CALL LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)


#STREAMLIT APP
st.title("✉️ Générateur d'Email")


#LES INPUTS
description = st.text_area("Décrivez en quelques mots le contenu de l'email que vous souhaitez générer")
ton = st.selectbox("Quel ton souhaitez-vous pour l'email ?", ["Formel", "Informel", "Amical", "Professionnel"])
longueur = st.slider("Quelle longueur pour l'email (en mots) ?", 50, 500, 150)


#INPUT FINAL
prompt = f"""Génère l'objet et le contenu d'un email en tenant compte de toutes ces informations :
Description : {description}
Ton : {ton}
Longueur : {longueur} mots

Ne dis rien d'autre, donne juste l'objet et le contenu de l'email.   """


if st.button("Générer email") : 
    reponse = llm.invoke(prompt).content
    st.success("email généré !")
    st.write(reponse)

