FROM jenkins/inbound-agent:latest

ARG DOCKER_GID=999

USER root

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    docker-cli \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd -g ${DOCKER_GID} docker \
    && usermod -aG docker jenkins

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/home/jenkins/.local/bin:${PATH}"

USER jenkins
