FROM python:3.10-alpine

# alpine系のライブラリは、apkでインストールする(ubuntuでいうところのapt-get).
# numpyのインストールで、gcc, musl-dev, linux-headersが必要になる.
# scipyのインストールで、gfortran, openblas-dev, cmake, ninjaが必要になる.
RUN apk --update add \
    curl \
    gcc \
    gfortran \
    musl-dev \
    linux-headers \
    build-base \
    libffi-dev \
    bash \
    openblas-dev \
    cmake \
    ninja \
    geos-dev \
    geos

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY ./dockerfiles/python/requirements.txt .

# Install the Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
