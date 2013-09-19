{% extends "os/os.tpl" %}

{% block dependencies %}
RUN apt-get update
RUN apt-get install -y build-essential libevent-dev openssh-server curl patch bzip2 libbz2-dev git siege sudo
#RUN apt-get install -y vim
{% endblock %}
