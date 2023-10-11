FROM python:3.11.2-slim-buster
# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# copy proejct
COPY . .