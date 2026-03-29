FROM debian:bookworm-slim

RUN apt-get update && apt-get install -y curl ca-certificates python3-minimal && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://openfang.sh/install | sh

ENV PATH="/root/.openfang/bin:${PATH}"

RUN mkdir -p /root/.openfang/hands/atlas
RUN mkdir -p /root/.openfang/skills/es-consulting/src

COPY config.toml /root/.openfang/config.toml
COPY SKILL.md /root/.openfang/hands/atlas/SKILL.md
COPY HAND.toml /root/.openfang/hands/atlas/HAND.toml
COPY skills/es-consulting/skill.toml /root/.openfang/skills/es-consulting/skill.toml
COPY skills/es-consulting/src/main.py /root/.openfang/skills/es-consulting/src/main.py
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
RUN chmod +x /root/.openfang/skills/es-consulting/src/main.py

EXPOSE 4200

CMD ["/entrypoint.sh"]
