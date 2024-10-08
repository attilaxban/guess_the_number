FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN chmod +x script.py
CMD ["python", "./script.py"]
