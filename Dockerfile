FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN apt-get update && rm -rf /var/lib/apt/lists/*
RUN pip install ./cloudflare-error-page
RUN pip install -e .

EXPOSE 5000
CMD ["python", "-m", "cloudflare_error_page_docker"]
