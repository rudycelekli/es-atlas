FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y curl ca-certificates && rm -rf /var/lib/apt/lists/*

# Install OpenFang
RUN curl -fsSL https://openfang.sh/install | sh

ENV PATH="/root/.openfang/bin:${PATH}"

# Create config directory
RUN mkdir -p /root/.openfang/hands/atlas

# Copy config and Atlas hand
COPY config.toml /root/.openfang/config.toml
COPY SKILL.md /root/.openfang/hands/atlas/SKILL.md
COPY HAND.toml /root/.openfang/hands/atlas/HAND.toml
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 4200

CMD ["/entrypoint.sh"]
