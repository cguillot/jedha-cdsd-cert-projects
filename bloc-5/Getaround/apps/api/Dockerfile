FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

RUN useradd -m -u 1000 user
USER user

ENV HOME=/home/user \
	PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

COPY --chown=user . $HOME/app

# Install the application dependencies.

# Need to copy root uv.lock at docker build
RUN uv sync --frozen --no-cache

# Huggingface default port
EXPOSE 7860

# Run the application.
CMD ["/home/user/app/.venv/bin/fastapi", "run", "/home/user/app/main.py", "--port", "7860", "--host", "0.0.0.0"]

# docker build -t  getaround-api .
# docker run -p 7860:7860  getaround-api

# // Allow the devcontainer to run host docker commands, see https://github.com/devcontainers/templates/tree/main/src/docker-outside-of-docker
# "features": {
#     "ghcr.io/devcontainers/features/docker-outside-of-docker:1": {}
# }
