FROM ghcr.io/astral-sh/uv:python3.13-alpine

WORKDIR /app
COPY . .

ENV UV_LINK_MODE copy
ENV UV_PROJECT_ENVIRONMENT /run/app/.venv
RUN apk --update --upgrade --no-cache add pango fontconfig ttf-freefont font-noto terminus-font \
    && uv sync --extra dev \
    && fc-cache -f

ENV PYTHONPATH /app/src
ENV PYTHONUNBUFFERED 1

ENTRYPOINT ["ash", "deployments/dev/backend/entrypoint.sh"]
