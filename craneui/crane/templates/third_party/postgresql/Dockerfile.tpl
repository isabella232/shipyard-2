{% extends 'third_party/third_party.tpl' %}

{% block debian %}
RUN sudo apt-get install -y postgresql
{% endblock%}

{% block redhat %}
{% endblock%}
