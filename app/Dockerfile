FROM python:latest

WORKDIR /app
COPY ["./requirements.txt", "."]
RUN pip3 install --no-cache-dir -r requirements.txt
COPY [".", "."]
CMD bash -c "while true; do sleep 1; done"

