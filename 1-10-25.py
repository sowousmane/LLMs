# A installer : 
#pip install langchain-google-genai
#pip install python-dotenv
# pip3 freeze > requirements.txt
######IMPORTATIONS
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

#CREER UN GENERATEUR D'HISTOIRE POUR ENFANTS
def generer_histoire(contexte) : 
    prompt = f"Invente une courte histoire intéressante sur ce sujet : {contexte} "


    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
    reponse = llm.invoke(prompt).content
    
    return reponse



histoire = generer_histoire("Les voitures volantes")
print(histoire)


