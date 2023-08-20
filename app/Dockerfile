FROM python:3.9-slim AS base
RUN apt-get update -y 
# also install curl and netcat for healthcheck or another software

FROM python:3.9-slim AS builder

WORKDIR /app
COPY app.py .

############### Build step done ###############
# The final image: we start clean
FROM base

# Create a non-root user to run the app and own app-specific files
RUN useradd -ms /bin/bash myuser
# Switch to this user
USER myuser

WORKDIR /home/app
COPY --chown=app . ./

EXPOSE 8000

CMD ["python", "app.py"]