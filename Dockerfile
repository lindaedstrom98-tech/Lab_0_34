FROM python:3.13-slim 

WORKDIR /app

COPY pyproject.toml .
COPY src ./src

RUN pip install .

EXPOSE 5000

CMD ["python", "src/api.py"]