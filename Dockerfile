# Utiliser une image Python de base
FROM python:3.9

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY streamlit_postgres.py /app/
COPY requirements.txt /app/

# Installer les dépendances
RUN pip install -r requirements.txt

# Exposer le port de Streamlit
EXPOSE 8501

# Commande pour lancer l’application
CMD ["streamlit", "run", "streamlit_postgres.py", "--server.port=8501", "--server.address=0.0.0.0"]

