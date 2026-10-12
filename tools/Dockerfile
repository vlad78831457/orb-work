FROM alpine:3.22
RUN apk add --no-cache git python3 py3-yaml
ENV HOME=/tmp GIT_OPTIONAL_LOCKS=0
RUN git config --system safe.directory '*'
WORKDIR /orb
