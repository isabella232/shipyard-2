{% extends "os/os.tpl" %}

{% block dependencies %}
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
{% endblock %}
