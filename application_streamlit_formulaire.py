import streamlit as st



st.title("Première application")

nom = st.text_input("Quel est votre nom ?")
description = st.text_area("Décrivez-vous en quelques mots")

age = st.slider("Quel est votre âge?", 0, 120,0)

etat_civil = st.selectbox("Quel est votre état civil ?", ["Célibataire", "Marié(e)", "Divorcé(e)", "Veuf(ve)"])

if st.button("Soumettre") : 
    st.success("Merci d'avoir fourni vos informations !")
    st.write(f"Bonjour {nom} !")
    st.write(f"Vous avez {age} ans et vous êtes {etat_civil}.")
    st.write("Description :")
    st.write(description)


#Exécution application streamlit
#streamlit run nom_app.py   --> Pour linux
#python -m streamlit run nom_app.py  --> Pour Windows