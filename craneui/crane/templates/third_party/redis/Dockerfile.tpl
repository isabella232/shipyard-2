{% extends 'third_party/third_party.tpl' %}

{% block debian %}
RUN apt-get install -y redis-server
{% endblock%}

{% block redhat %}
RUN yum install -y redis
{% endblock%}
