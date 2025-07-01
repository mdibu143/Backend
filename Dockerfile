FROM python:3.13.2-slim
RUN apt update -y && apt install -y net-tools curl lsof vim
WORKDIR /app
COPY . /app
RUN pip install -r requirement.txt
EXPOSE 8082
CMD ["uvicorn","main:app","--host", "0.0.0.0","--port","8082","--reload","--no-server-header"]