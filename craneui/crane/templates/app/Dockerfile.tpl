FROM {{repository}}/{{os}}/{{interpreter}}{{version}}

ADD . /home/qa/website
{% if git_url == 0 %}
ADD {{application_name}}.tar.gz /home/qa/website
{% else %}
RUN cd /home/qa/website && git clone {{git_url}}
{% endif %}

RUN chmod 755 /home/qa/website/buildapp.sh
RUN ls -l /home/qa/website
RUN chown -R qa:qa /home/qa/

# FIXME : sudo
#RUN sudo -u qa /home/qa/website/buildapp.sh
RUN /home/qa/website/buildapp.sh

RUN mv /home/qa/website/launch.sh /home/qa/website/{{application_name}}
RUN chmod 755 /home/qa/website/{{application_name}}/launch.sh

EXPOSE {{port}}

CMD /home/qa/website/{{application_name}}/launch.sh
