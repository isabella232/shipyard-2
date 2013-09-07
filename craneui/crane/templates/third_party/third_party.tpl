FROM {{repository}}/{{os}}

MAINTAINER New Relic Crane UI

ADD . /

{%- if os in ['debian', 'ubuntu']%}
{% block debian %}{%endblock%}
{%- elif os in ['redhat', 'centos']%}
{% block redhat %}{%endblock%}
{%- endif %}

EXPOSE {{port}}

VOLUME {{volume}}

CMD /launch.sh
