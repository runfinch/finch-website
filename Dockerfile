FROM public.ecr.aws/docker/library/python:3.11-slim-bullseye

# Install plugins
COPY requirements.txt .
RUN pip install -r requirements.txt
