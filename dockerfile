FROM python:3.10
#FROM docker/dev-environments-default:stable-1


RUN apt update \
    && apt install -y wget \
    && apt install -y unzip \
    && apt install -y vim \
    && apt install -y openssh-client \
    && apt install -y screen
   # && apt install -y python3-pip 

RUN apt install -qq -y curl
RUN apt install -y awscli 


# Download the latest version of Terraform from the official website
RUN wget https://releases.hashicorp.com/terraform/0.15.4/terraform_0.15.4_linux_amd64.zip

# Unzip the downloaded file:
RUN unzip terraform_0.15.4_linux_amd64.zip

# Move the terraform binary to a directory in your system's PATH.
RUN mv terraform /usr/local/bin/

# Verify that Terraform is installed by checking its version:
RUN terraform version

# Install python stuff
RUN pip install --upgrade pip
RUN pip install fastapi
RUN pip install uvicorn
RUN pip install kubernetes
RUN pip install --user virtualenv
RUN pip install "apache-airflow==2.8.0"
ENV AIRFLOW_HOME=/workspaces/DockerTest/DE-project/airflow
WORKDIR "/workspaces/DockerTest/DE-project/"
RUN screen -dm airflow standalone
# RUN fastapi fake data
WORKDIR "/workspaces/DockerTest/DE-project/api-data"
RUN screen -dm uvicorn api:app --reload --port 9000