FROM mcr.microsoft.com/devcontainers/python:1-3.12-bookworm

# The image ships a stale Yarn apt key that makes `apt-get update` fail, which breaks the sshd feature.
RUN rm -f /etc/apt/sources.list.d/yarn.*
