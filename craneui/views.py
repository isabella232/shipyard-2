from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.utils.translation import ugettext as _
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.utils.html import strip_tags
from django.core import serializers
from django.shortcuts import render_to_response
import django_rq
from django.template import RequestContext

from containers.models import Host

import crane.build
from crane.base import crane_path
from crane.inspect import list_versions, interpreter_extension
from craneui.forms import ApplicationBuildForm, OsBuildForm, InterpreterBuildForm, ThirdPartyForm

from shipyard import utils
from docker import client
from os import path, mkdir

import urllib
import random
import json
import tempfile

def build_on_hosts(to_apply, args, hosts):
    for i in hosts:
        host = Host.objects.get(id=i)
        local_args = args + (host.hostname, client_url(host))
        utils.get_queue('shipyard').enqueue(to_apply, args=local_args,
            timeout=3600)

def client_url(host):
    url ='{0}:{1}'.format(host.hostname, host.port)
    if not url.startswith('http'):
        url = 'http://{0}'.format(url)
    return url

@require_http_methods(['POST'])
@login_required
def build_os(request):
    '''
    Builds an os container image
    '''
    form = OsBuildForm(request.POST)
    os = form.data.get('os')
    hosts = form.data.getlist('hosts')

    args = (os,)
    build_on_hosts(crane.build.build_os, args, hosts)
    messages.add_message(request, messages.INFO,
        _('Building %s image.  This may take a few minutes.' % os))
    return redirect(reverse('index'))

@require_http_methods(['POST'])
@login_required
def build_interpreter(request):
    '''
    Builds an interpreter container image
    '''
    form = InterpreterBuildForm(request.POST)
    os = form.data.get('os')
    interpreter = form.data.get('interpreter')
    version = form.data.get('version')
    hosts = form.data.getlist('hosts')

    args = (interpreter, version, os)
    build_on_hosts(crane.build.build_interpreter, args, hosts)
    messages.add_message(request, messages.INFO,
        _('Building %s/%s%s image.  This may take a few minutes.' % (os, interpreter, version)))
    return redirect(reverse('index'))

def handle_upload(interpreter, application_archive, archive_name, application_name):
    application_folder = crane_path('build/app/%s/%s' % (interpreter, application_name))
    if not path.exists(application_folder):
       mkdir(application_folder, 0755)

    tmp_file = path.join(application_folder, archive_name)
    with open(tmp_file, 'w') as d:
        for c in application_archive.chunks():
            d.write(c)

@require_http_methods(['POST'])
@login_required
def build_application(request):
    '''
    Builds an application container image
    '''
    form = ApplicationBuildForm(request.POST)
    os = form.data.get('os')
    interpreter = form.data.get('interpreter')
    version = form.data.get('version')
    port = form.data.get('port')
    launch = form.data.get('launch')
    before_launch = form.data.get('before_launch')
    after_launch = form.data.get('after_lauch')
    hosts = form.data.getlist('hosts')
    archive = request.FILES.get('application')
    git_url = form.data.get('git_url')
        
    if archive:
       archive_name = request.FILES.get('application').name
       application_name = archive_name.split('.')[0]
       handle_upload(interpreter, archive, archive_name, application_name)
    elif git_url:
       application_name = git_url.split('/')[-1].split('.')[0]
    else:
       pass # FIXME add error

    args = (interpreter, version, os, port, application_name, launch, after_launch, before_launch, git_url)
    build_on_hosts(crane.build.build_application, args, hosts)
    messages.add_message(request, messages.INFO,
        _('Building %s/%s%s/%s image.  This may take a few minutes.' % (os, interpreter, version, application_name)))
    return redirect(reverse('index'))

@require_http_methods(['POST'])
@login_required
def build_third(request):
    '''
    Builds a third party software container image
    '''
    form = ThirdPartyBuildForm(request.POST)
    os = form.data.get('os')
    software = form.data.get('software')
    hosts = form.data.getlist('hosts')

    args = (os, software, hosts)
    build_on_hosts(crane.build.build_third, args, hosts)
    messages.add_message(request, messages.INFO,
        _('Building %s image.  This may take a few minutes.' % software))
    return redirect(reverse('index'))

def versions(request):
    return HttpResponse(
            json.dumps({'versions' : list_versions(request.GET['interpreter'])})
           ,mimetype="application/json")

def extensions(request):
    return HttpResponse(
            json.dumps({'extension' : interpreter_extension(request.GET['interpreter'])})
           ,mimetype="application/json")
