FROM python:3-slim

WORKDIR /app

# Copier le fichier requirements.txt
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Ne pas spécifier d'ENTRYPOINT pour plus de flexibilité
