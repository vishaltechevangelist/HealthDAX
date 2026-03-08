FROM python:3.11-slim-bookworm

WORKDIR /app

RUN apt-get update && apt-get upgrade -y && apt-get clean

COPY requirements.txt .

RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7860
EXPOSE 8000

CMD ["bash","run.sh"]