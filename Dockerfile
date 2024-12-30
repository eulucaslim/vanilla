FROM python3.10-slim

WORKDIR /vanilla
COPY requirements.txt /vanilla/requirements.txt
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get remove -y build-essential && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . /vanilla
CMD ['python' 'manage.py', 'runserver']