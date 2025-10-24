# Étape 1 : image Python légère
FROM python:3.11-slim

# Étape 2 : installer les dépendances système pour Chrome
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    ca-certificates \
    fonts-liberation \
    libnss3 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxrandr2 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdbus-1-3 \
    libgtk-3-0 \
    libgbm1 \
    libpangocairo-1.0-0 \
    libxshmfence1 \
    libxss1 \
    libxext6 \
    libxfixes3 \
    lsb-release \
    && rm -rf /var/lib/apt/lists/*

# Étape 3 : installer Google Chrome via .deb
RUN wget -O /tmp/google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get update \
    && apt-get install -y /tmp/google-chrome.deb \
    && rm /tmp/google-chrome.deb \
    && apt-get clean

# Étape 4 : définir le répertoire de travail
WORKDIR /app

# Étape 5 : copier le code et requirements
COPY . .

# Étape 6 : installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Étape 7 : commande par défaut
CMD ["python", "scraper.py"]
