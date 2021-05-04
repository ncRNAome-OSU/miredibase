ARG PYTHON_VERSION=3.8

FROM python:${PYTHON_VERSION} AS builder
ENV PYTHONUNBUFFERED=1
WORKDIR /wheels
COPY requirements.txt .
RUN pip install -U pip \
    && pip wheel -r requirements.txt

FROM python:${PYTHON_VERSION}-slim
ENV PYTHONUNBUFFERED=1
COPY --from=builder /wheels /wheels
RUN pip install -U pip \
    && pip install -r /wheels/requirements.txt -f /wheels \
    && rm -rf /wheels \
    && rm -rf /root/.cache/pip/* 

ENV USER=docker
ENV GROUP=docker
ENV UID=85647
ENV GID=20475
ENV HOME=/mbapi
WORKDIR ${HOME}

RUN addgroup --gid "${GID}" "${GROUP}" \
    && adduser \
    --disabled-password \
    --gecos "" \
    --home "$(pwd)" \
    --ingroup "${GROUP}" \
    --no-create-home \
    --uid "${UID}" \
    "${USER}" \
    && rm ${HOME}/Dockerfile ${HOME}requirements.txt

USER ${USER}

COPY --chown=docker:docker api .
COPY --chown=docker:docker config .
COPY --chown=docker:docker main.py .
