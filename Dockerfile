# Använd en officiell, lättviktig Python-miljö som grund
FROM python:3.9-slim

# Bestäm vilken mapp i containern vi ska arbeta i
WORKDIR /app

# Kopiera in filerna från din Mac till containern
COPY pyproject.toml .
COPY src/ src/

# Installera Flask inuti containern
RUN pip install flask

# Tala om att containern kommer att använda port 5000
EXPOSE 5000

# Kommandot som körs när containern startas
CMD ["flask", "--app", "src/api", "run", "--host=0.0.0.0"]