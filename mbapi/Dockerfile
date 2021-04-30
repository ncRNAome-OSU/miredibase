FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN mkdir /mbapi && python3.8 -m pip install pip==21.1
WORKDIR /mbapi
COPY api /mbapi/
COPY config /mbapi/
COPY main.py /mbapi/
COPY requirements.txt /mbapi/

RUN pip install -r requirements.txt







FROM python:3.8-slim AS compile-image
ENV PYTHONUNBUFFERED 1

ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3 -m venv $VIRTUAL_ENV

COPY requirements.txt .
RUN python3 -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

FROM python:3.8-slim AS build-image
ENV VIRTUAL_ENV=/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN mkdir /mbapi
WORKDIR /mbapi
COPY api .
COPY config .
COPY main.py .

COPY --from=compile-image $VIRTUAL_ENV $VIRTUAL_ENV











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
    "${USER}"

USER ${USER}

COPY api .
COPY config .
COPY main.py .

RUN chown -R docker:docker *
