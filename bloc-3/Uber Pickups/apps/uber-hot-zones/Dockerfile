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

# Run the application. --client.toolbarMode=minimal --ui.hideTopBar=True
CMD ["/home/user/app/.venv/bin/streamlit", "run", "--server.port", "7860", "/home/user/app/main.py", "--client.toolbarMode", "minimal", "--ui.hideTopBar", "True"]

# docker build -t  uber-rides-dashboard .
# docker run -p 7860:7860  uber-rides-dashboard
