FROM public.ecr.aws/docker/library/python:3.12-slim-bullseye

# Install plugins
COPY requirements.txt .
RUN pip install -r requirements.txt
