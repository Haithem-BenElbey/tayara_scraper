# Image officielle Python
FROM python:3.11-slim

# Variables d'environnement pour éviter les prompts et les caches inutiles
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

# Créer le dossier de travail
WORKDIR /app

# Copier requirements et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code
COPY . .

# Créer un dossier pour les fichiers générés
RUN mkdir -p /app/data

# Définir le script à exécuter par défaut
CMD ["python", "main.py"]
