# Use the Python 3.7 image as the base
FROM python:3.7-bullseye

# Mise à jour et installation des dépendances nécessaires
RUN apt-get update && \
    apt-get install -y python3-pip git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install PyTorch and PyTorch CUDA
RUN conda install pytorch pytorch-cuda=11.8 -c pytorch -c nvidia

# ------------------------------------------------------------------------------
# Install Cytomine python client
RUN git clone https://github.com/cytomine-uliege/Cytomine-python-client.git && \
    cd Cytomine-python-client/ && git checkout tags/v2.7.3 && pip install . && \
    rm -rf /Cytomine-python-client

# ------------------------------------------------------------------------------
# Install BIAFLOWS utilities (annotation exporter, compute metrics, helpers,...)
RUN apt-get update && apt-get install -y libgeos-dev && apt-get clean
RUN git clone https://github.com/Neubias-WG5/biaflows-utilities.git && \
    cd biaflows-utilities/ && git checkout tags/v0.9.2 && pip install . --no-deps

# install utilities binaries
RUN chmod +x biaflows-utilities/bin/*
RUN cp biaflows-utilities/bin/* /usr/bin/ && \
    rm -r biaflows-utilities/

# ------------------------------------------------------------------------------

# Installation de biom3d 
RUN pip install biom3d

# Ajout des fichiers de l'application
ADD wrapper.py /app/wrapper.py
ADD descriptor.json /app/descriptor.json

ENTRYPOINT ["python3.7","/app/wrapper.py"]
