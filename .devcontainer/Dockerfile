ARG PYTHON_VERSION="3.12"

FROM mcr.microsoft.com/vscode/devcontainers/python:${PYTHON_VERSION}-bullseye
ENV VIRTUAL_ENV=/home/dev/.local \
    PATH=$VIRTUAL_ENV/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    DEBIAN_FRONTEND=noninteractive \
    TZ=Europe/Berlin

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
    && pip install --upgrade pip \
    && pip install uv \
    && rm /usr/bin/python3 && ln -s /usr/local/bin/python /usr/bin/python \
    && usermod -l dev -d /home/dev -m vscode \
    && sed -i 's/vscode/dev/' /etc/sudoers.d/vscode \
    && mv /etc/sudoers.d/vscode /etc/sudoers.d/dev \
    # Create .zfunc directory and add it to the fpath to have zsh autocompletions
    && mkdir -p /home/dev/.zfunc && chown dev:vscode /home/dev/.zfunc \
    && echo "\nfpath+=~/.zfunc\nautoload -Uz compinit && compinit\n" >> /home/dev/.zshrc \
    # Set python __pycache__ directory to $HOME/.cache/cpython
    && echo 'export PYTHONPYCACHEPREFIX="$HOME/.cache/cpython/"' | tee -a /home/dev/.profile /home/dev/.zshrc /home/dev/.bashrc \
    # Add autoload of .env to .profile, .zshrc and .bashrc
    && echo 'export $(grep -v "^#" /aoc/.env | xargs) 2> /dev/null' | tee -a /home/dev/.profile /home/dev/.bashrc \
    && echo 'preexec() { export $(grep -v "^#" /eventbridge/.env | xargs) 2> /dev/null; }' | tee -a /home/dev/.zshrc \
    && sed -i 's/${prompt_username}/λ/g' /home/dev/.oh-my-zsh/custom/themes/devcontainers.zsh-theme \
    # Create marker file to indicate that the postCreateCommand will run (used in .vscode/tasks.json)
    && touch /home/dev/.postCreateCommandRunning \
    # # # Install Java, used in serverless-offline-sqs
    # && apt-get update && apt-get install default-jre -y \
    # && apt-get autoremove -y && apt-get clean -y \
    # && wget https://s3-eu-west-1.amazonaws.com/softwaremill-public/elasticmq-server-1.6.7.jar -q -O /home/dev/elasticmq-server.jar
