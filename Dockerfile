FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y wget curl unzip gnupg ca-certificates fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 libnspr4 libnss3 libxss1 libxcomposite1 libxcursor1 libxdamage1 libxi6 libxtst6 xdg-utils && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    dpkg -i google-chrome-stable_current_amd64.deb || apt-get install -yf && \
    rm google-chrome-stable_current_amd64.deb && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV CHROME_BIN=/usr/bin/google-chrome

EXPOSE 10000

CMD ["python", "app.py"]
