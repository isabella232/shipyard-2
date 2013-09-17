FROM ubuntu

MAINTAINER New Relic Crane UI

ENV BUILD 

RUN useradd qa --home /home/qa/ --shell `which bash` --groups sudo
RUN mkdir /home/qa
RUN chown -R qa /home/qa

RUN echo 'root:toor' | chpasswd
RUN echo 'qa:aq' | chpasswd

RUN apt-get update
RUN apt-get install -y build-essential
RUN apt-get install -y libevent-dev
RUN apt-get install -y openssh-server
RUN apt-get install -y curl
RUN apt-get install -y patch
RUN apt-get install -y bzip2 libbz2-dev
RUN apt-get install -y git
RUN apt-get install -y siege
RUN apt-get install -y sudo
#RUN apt-get install -y vim

RUN mkdir /var/run/sshd

EXPOSE 22

RUN echo $BUILD

CMD ["/usr/sbin/sshd", "-D"]