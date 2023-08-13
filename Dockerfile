FROM python:3.11-slim-bullseye as stage-build
ARG TARGETARCH

ARG BUILD_DEPENDENCIES="              \
        g++                           \
        make                          \
        pkg-config"

ARG DEPENDENCIES="                    \
        freetds-dev                   \
        libpq-dev                     \
        libffi-dev                    \
        libjpeg-dev                   \
        libkrb5-dev                   \
        libldap2-dev                  \
        libsasl2-dev                  \
        libssl-dev                    \
        libxml2-dev                   \
        libxmlsec1-dev                \
        libxmlsec1-openssl            \
        freerdp2-dev                  \
        libaio-dev"

ARG TOOLS="                           \
        ca-certificates               \
        curl                          \
        default-libmysqlclient-dev    \
        default-mysql-client          \
        git                           \
        git-lfs                       \
        unzip                         \
        xz-utils                      \
        wget"

ARG APT_MIRROR=http://mirrors.ustc.edu.cn

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked,id=core \
    sed -i "s@http://.*.debian.org@${APT_MIRROR}@g" /etc/apt/sources.list \
    && rm -f /etc/apt/apt.conf.d/docker-clean \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && apt-get update \
    && apt-get -y install --no-install-recommends ${BUILD_DEPENDENCIES} \
    && apt-get -y install --no-install-recommends ${DEPENDENCIES} \
    && apt-get -y install --no-install-recommends ${TOOLS} \
    && echo "no" | dpkg-reconfigure dash \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /opt

ARG RUST_VERSION=1.65.0
RUN set -ex \
    && cd /opt \
    && \
    if [ "${TARGETARCH}" == "s390x" ] || [ "${TARGETARCH}" == "ppc64le" ] || [ "${TARGETARCH}" == "loong64" ]; then \
        rustUrl="https://static.rust-lang.org/dist"; \
        rustArch="${TARGETARCH}"; \
        mkdir -p /opt/rust-install; \
        if [ "${TARGETARCH}" == "loong64" ]; then \
            rustUrl="https://rust-lang.loongnix.cn/dist/2022-11-03"; \
            rustArch="loongarch64"; \
        fi; \
        if [ "${TARGETARCH}" == "ppc64le" ]; then \
            rustArch="powerpc64le"; \
        fi; \
        wget -O /opt/rust.tar.gz "${rustUrl}/rust-${RUST_VERSION}-${rustArch}-unknown-linux-gnu.tar.xz"; \
        tar -xf /opt/rust.tar.gz -C /opt/rust-install --strip-components=1; \
        cd /opt/rust-install && ./install.sh; \
        cd /opt; \
        rm -rf /opt/rust.tar.gz /opt/rust-install; \
    fi

ARG VERSION
ENV VERSION=$VERSION

WORKDIR /opt/jumpserver
ADD . .
RUN cd utils && bash -ixeu build.sh

ARG PIP_MIRROR=https://pypi.tuna.tsinghua.edu.cn/simple
RUN --mount=type=cache,target=/root/.cache \
    set -ex \
    && pip install poetry -i ${PIP_MIRROR} \
    && poetry config virtualenvs.create false \
    && poetry install

FROM python:3.11-slim-bullseye
ARG TARGETARCH

ARG DEPENDENCIES="                    \
        libxmlsec1-openssl"

ARG TOOLS="                           \
        ca-certificates               \
        curl                          \
        default-libmysqlclient-dev    \
        default-mysql-client          \
        inetutils-ping                \
        locales                       \
        openssh-client                \
        procps                        \
        sshpass                       \
        telnet                        \
        unzip                         \
        vim                           \
        nmap                          \
        wget"

ARG APT_MIRROR=http://mirrors.ustc.edu.cn

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked,id=core \
    sed -i "s@http://.*.debian.org@${APT_MIRROR}@g" /etc/apt/sources.list \
    && rm -f /etc/apt/apt.conf.d/docker-clean \
    && ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && apt-get update \
    && apt-get -y install --no-install-recommends ${DEPENDENCIES} \
    && apt-get -y install --no-install-recommends ${TOOLS} \
    && mkdir -p /root/.ssh/ \
    && echo "Host *\n\tStrictHostKeyChecking no\n\tUserKnownHostsFile /dev/null\n\tCiphers +aes128-cbc\n\tKexAlgorithms +diffie-hellman-group1-sha1\n\tHostKeyAlgorithms +ssh-rsa" > /root/.ssh/config \
    && echo "set mouse-=a" > ~/.vimrc \
    && echo "no" | dpkg-reconfigure dash \
    && echo "zh_CN.UTF-8" | dpkg-reconfigure locales \
    && sed -i "s@# export @export @g" ~/.bashrc \
    && sed -i "s@# alias @alias @g" ~/.bashrc \
    && rm -rf /var/lib/apt/lists/*

COPY --from=stage-build /opt/jumpserver/release/jumpserver /opt/jumpserver
WORKDIR /opt/jumpserver

ARG PIP_MIRROR=https://pypi.douban.com/simple
RUN --mount=type=cache,target=/root/.cache \
    set -ex \
    && echo > /opt/jumpserver/config.yml \
    && pip install poetry -i ${PIP_MIRROR} \
    && poetry config virtualenvs.create false \
    && poetry install --only=main

VOLUME /opt/jumpserver/data
VOLUME /opt/jumpserver/logs

ENV LANG=zh_CN.UTF-8

EXPOSE 8080

ENTRYPOINT ["./entrypoint.sh"]
