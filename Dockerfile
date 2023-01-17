FROM python:3.9
WORKDIR /workdir
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt
