# cloudflare-error-page-docker

Flask server that serves customizable Cloudflare-style error pages using [cloudflare-error-page](https://github.com/donlon/cloudflare-error-page).

## Usage

### Docker

```bash
docker-compose up
```

Access at `http://localhost:8080`

### Python

```bash
git submodule update --init --recursive
pip install ./cloudflare-error-page
pip install -e .
python -m cloudflare_error_page_docker
```

## Endpoints

- `/` - Default error page
- `/<code>.html` - Error page with custom code (e.g., `/404.html`, `/503.html`)
- `/health` - Health check

## Configuration

Edit `params.json` to customize the error page.

See [cloudflare-error-page documentation](https://github.com/donlon/cloudflare-error-page) for available parameters.

## Environment Variables

- `HOST` - Bind host (default: `0.0.0.0`)
- `PORT` - Bind port (default: `5000`)
