# Image de base officielle de PyTorch
FROM pytorch/pytorch:latest

# Mise à jour et installation des dépendances nécessaires
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-pip

# Installation de biom3d 
RUN pip install biom3d

# Répertoire de travail 
WORKDIR /workspace

# Commande pour garder le conteneur en marche 
CMD ["tail", "-f", "/dev/null"]
