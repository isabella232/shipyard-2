FROM {{os}}

MAINTAINER New Relic Crane UI

RUN useradd qa --home /home/qa/ --shell `which bash`
RUN mkdir /home/qa
RUN chown -R qa /home/qa

RUN echo 'root:toor' | chpasswd
RUN echo 'qa:aq' | chpasswd
{% block dependencies %}
{% endblock %}
RUN mkdir /var/run/sshd

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
