# Use an official Python runtime as a parent image
FROM python:3.6

MAINTAINER Bongani Sibanda <sibandabongz@gmail.com>

WORKDIR /usr/local/nameko_test_service

COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["nameko", "run", "--config", "conf.yml", "test_service.serve"]
