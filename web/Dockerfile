FROM python:3.9.2 AS builder

ENV PYTHONBUFFERED 1

COPY requirements.txt .
RUN mkdir pip_cache
RUN pip install --upgrade pip
RUN pip install --user -r requirements.txt --cache-dir $HOME/pip_cache

FROM python:3.9.2-slim-buster
WORKDIR /web

COPY --from=builder /root/.local /root/.local
COPY ./src .

ENV PATH=/root/.local:$PATH
ENV PATH=/root/.local/bin:$PATH

CMD ["python", "manage.py", "runserver 0.0.0.0:8000"]