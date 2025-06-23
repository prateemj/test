FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y wget curl unzip gnupg && \
    wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -u && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" \
      > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 10000

CMD ["python", "app.py"]
