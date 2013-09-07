from base import crane_path
from os import path, mkdir
from jinja2 import Environment, FileSystemLoader

"""
In this file are all the function use to render the crane templates:
Dockerfiles, scripts, etc
"""

jinja_env = Environment(loader=FileSystemLoader([crane_path('templates'), crane_path('build')]))

OS_TPL = 'os/%s.tpl'
INTERPRETER_TPL = 'interpreter/%s/%s.tpl'
APP_TPL = 'app/Dockerfile.tpl'

DEFAULT_PORT = 5000

#   Dockerfiles -----------------------------------------------------------------------------------

def render_template__(template, **variables):
    """
    A simple helper to render the templates with the crane Environment.
    """
    return jinja_env.get_template(template).render(variables)

def os_Dockerfile(os):
    """
    Render the Dockerfile that install an os in a container.
    """
    return render_template__(OS_TPL % os, **locals())

def interpreter_Dockerfile(interpreter, version, os, repository):
    """
    Render the Dockerfile that install an interpreter version in a container.
    """
    return render_template__(INTERPRETER_TPL % (interpreter, interpreter), **locals())

def application_Dockerfile(interpreter, version, os, repository, application_name, port = DEFAULT_PORT):
    """
    Render the Dockerfile for the container
    """
    return render_template__(APP_TPL, **locals())

#   Scripts -----------------------------------------------------------------------------------

INTERPRETER_SCRIPT = 'interpreter/%s/install.sh'
APP_BUILD_SCRIPT = 'app/%s/buildapp.sh'
APP_LAUNCH_SCRIPT = 'app/%s/launch.sh'

def interpreter_install_script(interpreter):
    """
    Render the script that install an interpreter version and its package/version manager.
    """
    return render_template__(INTERPRETER_SCRIPT % interpreter, **{}) # No need for variables here


def application_install_script(interpreter, application_name, configuration):
    """
    Render the script that install the app into the container. 
    """
    return render_template__(APP_BUILD_SCRIPT % interpreter, **locals())


def application_launch_script(interpreter, launch, after_launch):
    """
    Render the script that will be use when the container is launched.
    """
    return render_template__(APP_LAUNCH_SCRIPT % interpreter, **locals())
