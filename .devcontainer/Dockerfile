# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.224.3/containers/ubuntu/.devcontainer/base.Dockerfile

# [Choice] Ubuntu version (use hirsuite or bionic on local arm64/Apple Silicon): hirsute, focal, bionic
ARG VARIANT="focal"
FROM mcr.microsoft.com/vscode/devcontainers/base:0-${VARIANT}

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#      && apt-get -y install --no-install-recommends hugo

RUN wget https://github.com/gohugoio/hugo/releases/download/v0.97.3/hugo_extended_0.97.3_Linux-64bit.deb && dpkg -i hugo_extended_0.97.3_Linux-64bit.deb