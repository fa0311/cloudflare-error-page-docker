FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install ./cloudflare-error-page
RUN pip install -e .

HEALTHCHECK --interval=1m --timeout=5s --start-period=20s --retries=1 CMD curl -S http://localhost:5000
EXPOSE 5000
CMD ["python", "-m", "cloudflare_error_page_docker"]
