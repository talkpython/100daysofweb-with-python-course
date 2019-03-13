FROM ubuntu:latest

RUN apt-get update && apt-get upgrade -y
ENV TZ=America/Los_Angeles
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get install -y -q sudo
RUN apt-get install -y -q fail2ban
RUN apt-get install -y -q httpie
RUN apt-get install -y -q glances
