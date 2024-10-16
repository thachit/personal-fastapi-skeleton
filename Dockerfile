FROM python:3.9.9-buster
RUN mkdir -p /fastapi_learning
WORKDIR /fastapi_learning
COPY . .
RUN ls -la
RUN apt-get update
RUN apt-get install -y  --no-install-recommends --no-install-suggests gcc autoconf libc6-dev curl libssl-dev libffi-dev

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip install -r requirements.txt
CMD ["uvicorn", "src.app:fast_api","--host=0.0.0.0", "--port=8002", "--log-level=debug", "--workers=1", "--timeout-keep-alive=60"]