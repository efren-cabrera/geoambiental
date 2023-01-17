FROM python:3.9
WORKDIR /workdir
COPY . .
RUN pip install --upgrade pip && pip install \
    black \
    codecov \
    flake8 \
    geopy \
    matplotlib \
    mutmut \
    mypy \
    pylint \
    pytest \
    pytest-cov \
    utm 
