FROM python:3.10-slim

#To force Python to print output immediately, you can set the PYTHONUNBUFFERED environment variable
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY echo_server.py .

CMD ["python", "echo_server.py"]
