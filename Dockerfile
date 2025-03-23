FROM python:3.11

ENV PROJECT_ROOT="/opt/ws-ml-api/"
ENV PYTHONPATH=${PYTHONPATH}:${PROJECT_ROOT}

WORKDIR ${PROJECT_ROOT}

COPY requirements.txt ./

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    && pip install -r requirements.txt

RUN apt-get autoremove -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/*

ADD . ./

EXPOSE 8080

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8080", "src.main:app"]
