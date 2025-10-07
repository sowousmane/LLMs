# Projet LLMs

## Description
Ce projet contient plusieurs scripts Python et fichiers de configuration pour travailler avec des modèles de langage (LLMs). Il inclut des fonctionnalités telles que la génération d'e-mails, un chatbot, et des configurations Docker pour déployer les services.

## Structure du projet

- **1-10-25.py** : Script Python pour une tâche spécifique (à détailler).
- **app-one-2-10-25.py** : Script Python pour une autre tâche spécifique (à détailler).
- **call.py** : Script Python pour gérer les appels ou les interactions.
- **chatbot.py** : Implémentation d'un chatbot utilisant des modèles de langage.
- **generate-email.py** : Script Python pour générer des e-mails automatiquement.
- **Dockerfile** : Fichier de configuration Docker pour créer une image du projet.
- **docker-compose.yml** : Fichier de configuration Docker Compose pour orchestrer les services.
- **requirements.txt** : Liste des dépendances Python nécessaires au projet.

## Prérequis

- Python 3.8 ou supérieur
- Docker et Docker Compose

## Installation

1. Clonez le dépôt :
   ```bash
   git clone <URL_DU_DEPOT>
   cd LLMs
   ```

2. Construisez et démarrez les services Docker :
   ```bash
   docker-compose up --build
   ```

3. Connectez-vous au conteneur en bash :
   ```bash
   docker exec -it <nom_du_conteneur> bash
   ```

4. Installez les dépendances dans le conteneur :
   ```bash
   pip install -r requirements.txt
   ```

5. Lancez les scripts :
   - Pour les fichiers Python :
     ```bash
     python <nom_du_fichier>.py
     ```
   - Pour les fichiers Streamlit :
     ```bash
     streamlit run <nom_du_fichier>.py
     ```

## Utilisation

- **Chatbot** : Exécutez `chatbot.py` pour démarrer le chatbot.
- **Génération d'e-mails** : Utilisez `generate-email.py` pour générer des e-mails.
- **Autres scripts** : Consultez les fichiers pour plus de détails sur leur utilisation.

## Contribution

1. Forkez le projet.
2. Créez une branche pour vos modifications :
   ```bash
   git checkout -b feature/nom-de-la-fonctionnalite
   ```
3. Soumettez une pull request.
