FROM {{repository}}/{{os}}/{{interpreter}}{{version}}

{# Dirty hardcoded installation #}
RUN sudo apt-get install -y mysql-server libmysqlclient-dev sqlite3 libsqlite3-dev

EXPOSE 3306

ADD . /home/qa/website
{% if not git_url %}
ADD {{application_name}}.tar.gz /home/qa/website
{% else %}
RUN cd /home/qa/website && git clone {{git_url}}
{% endif %}

RUN chown -R qa:qa /home/qa/ && chmod 755 /home/qa/website/buildapp.sh && sudo -u qa /home/qa/website/buildapp.sh

RUN mv /home/qa/website/launch.sh /home/qa/website/{{application_name}} && chmod 755 /home/qa/website/{{application_name}}/launch.sh
RUN mv /home/qa/website/launcher.sh /home/qa/website/{{application_name}} && chmod 755 /home/qa/website/{{application_name}}/launcher.sh

EXPOSE {{port}}

VOLUME '/home/qa/databases'

CMD /home/qa/website/{{application_name}}/launcher.sh
