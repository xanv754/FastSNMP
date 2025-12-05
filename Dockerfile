FROM python:3.13-slim AS builder

WORKDIR /app

RUN pip install --no-cache-dir pip-tools
COPY pyproject.toml .
RUN pip-compile --output-file=requirements.txt pyproject.toml

FROM python:3.13-slim

WORKDIR /app

COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN pip install -e .

CMD ["uvicorn", "fast_snmp.api.app:app", "--host", "0.0.0.0", "--port", "8000"]
