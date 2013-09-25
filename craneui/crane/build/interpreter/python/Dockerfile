FROM 127.0.0.1/ubuntu

ADD . /install
RUN chmod 755 /install/install.sh

RUN apt-get update > /dev/null
RUN apt-get install -y build-essential libsqlite3-dev libreadline-gplv2-dev libncurses5-dev zlib1g-dev libbz2-dev libssl-dev libgdbm-dev libsasl2-dev

RUN /install/install.sh 3.3.2

RUN ln -s /usr/local/bin/python3 /usr/local/bin/python

RUN wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | python
RUN easy_install pip
RUN pip install virtualenv
RUN pip install virtualenvwrapper