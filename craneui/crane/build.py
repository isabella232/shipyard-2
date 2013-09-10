from docker import client
from base import crane_path
from os import path, mkdir
import render

def save_in(filename, string):
    f = open(filename, 'w')
    f.write(string)

# FIXME : if build_path NOT exists, mkdir?
def build(client_url, repository, result, build_path, variables, tag):
    """
    Prepare and build a container based on a Dockerfile.
    """
    docker_client = client.Client(base_url=client_url, version="1.3")
    print "Building : '%s/%s'" % (repository, tag)
    save_in('%s/Dockerfile' % build_path, result)
    match, log = docker_client.build(path=build_path)
    if match != None:
       print 'Container id : %s' % match
       print docker_client.tag(match, '%s/%s' % (repository, tag));
    print "Building is finished"
    return log

def build_os(os, repository, client_url):
    """
    Build an os container based on a Dockerfile.
    """
    os_path = crane_path('build/os/%s' % os)
    Dockerfile = render.os_Dockerfile(os)
    return build(client_url, repository, Dockerfile, os_path, {'os' : os} , os)
    
def build_interpreter(interpreter, version, os, repository, client_url):
    """
    Build a interpreter container based on a Dockerfile.
    """
    tag = '%s/%s' % (os, interpreter + version)
    interpreter_path = crane_path('build/interpreter/%s' % interpreter)

    save_in(path.join(interpreter_path, 'install.sh'), render.interpreter_install_script(interpreter))
    Dockerfile = render.interpreter_Dockerfile(interpreter, version, os, repository)
    return build(client_url, repository, Dockerfile, interpreter_path, locals(), tag)

def build_application(interpreter
                     ,version
                     ,os
                     ,port
                     ,application_name
                     ,launch
                     ,after_launch
                     ,before_launch
                     ,git_url
                     ,repository
                     ,client_url):
    """
    Build an application container based on a Dockerfile.
    """
    application_folder = crane_path('build/app/%s/%s' % (interpreter, application_name))
    if not path.exists(application_folder):
       mkdir(application_folder, 0755)

    save_in('%s/buildapp.sh' % application_folder
           ,render.application_install_script(interpreter, application_name, before_launch))
    save_in('%s/launch.sh' % application_folder
           ,render.application_launch_script(interpreter, launch, after_launch))

    tag = '%(os)s/%(interpreter)s%(version)s/%(application_name)s' % (locals())
    Dockerfile = render.application_Dockerfile(interpreter, version, os, repository, application_name, git_url, port)
    return build(client_url, repository, Dockerfile, application_folder, locals(), tag)
