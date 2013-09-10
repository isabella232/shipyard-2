from django import forms
from containers.models import Host
from containers.forms import get_available_hosts
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field, Div
from crispy_forms.bootstrap import FieldWithButtons, StrictButton
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _

from crane.inspect import list_oses, list_interpreters, list_versions, interpreter_extension

oses = list_oses()
interpreters = list_interpreters()
interpreter_name = interpreters[0][1]
extension = interpreter_extension(interpreter_name)
versions = list_versions(interpreter_name)

class OsBuildForm(forms.Form):
      os = forms.ChoiceField(choices=oses)
      hosts = forms.MultipleChoiceField(choices=[(x.id, x.name) for x in get_available_hosts()])

      def __init__(self, *args, **kwargs):
          super(OsBuildForm, self).__init__(*args, **kwargs)
          self.helper = FormHelper()
          self.helper.form_id = 'form-build-os'
          self.helper.form_class = 'form-horizontal' # FIXME : horizontal?
          self.helper.form_action = reverse('craneui.views.build_os')
          self.helper.help_text_inline = True

class InterpreterBuildForm(forms.Form):
      os = forms.ChoiceField(choices=oses)
      interpreter = forms.ChoiceField(choices=interpreters)
      version = forms.ChoiceField(choices=versions)
      hosts = forms.MultipleChoiceField(choices=[(x.id, x.name) for x in get_available_hosts()])

      def __init__(self, *args, **kwargs):
          super(InterpreterBuildForm, self).__init__(*args, **kwargs)
          self.helper = FormHelper()
          self.helper.form_id = 'form-build-interpreter'
          self.helper.form_class = 'form-horizontal' # FIXME : horizontal?
          self.helper.form_action = reverse('craneui.views.build_interpreter')
          self.helper.help_text_inline = True
          # FIXME : inline interpreter/version
          self.helper.layout = Layout(
               'os',
               Field('interpreter', css_class="input-small", id="interpreter_interpreter"),
               Field('version', css_class="input-small", id="interpreter_version", label=""),
               'hosts')

class ApplicationBuildForm(forms.Form):
      os = forms.ChoiceField(choices=oses)
      interpreter = forms.ChoiceField(choices=interpreters)
      version = forms.ChoiceField(choices=versions, label=None)
      application = forms.FileField('application')
      git_url = forms.CharField()
      port = forms.CharField(initial=5000)
      launch = forms.CharField(initial="%s app.%s" % (interpreter_name, extension))
      after_launch = forms.CharField(initial="siege --concurrent 2 --delay 1 -f urls.txt", required = False)
      before_launch = forms.CharField(initial="%s db.%s" % (interpreter_name, extension), required=False)
      hosts = forms.MultipleChoiceField(choices=[(x.id, x.name) for x in get_available_hosts()])

      def __init__(self, *args, **kwargs):
          super(ApplicationBuildForm, self).__init__(*args, **kwargs)
          self.helper = FormHelper()
          self.helper.form_id = 'form-build-application'
          self.helper.form_class = 'form-horizontal' # FIXME : horizontal?
          self.helper.form_action = reverse('craneui.views.build_application')
          self.helper.help_text_inline = True
          # FIXME : inline interpreter/version
          self.helper.layout = Layout(
               'os',
#               Div(
#                    Div(Field('interpreter', css_class="span12", id="application_interpreter"), css_class="span6"),
#                    Div(Field('version', css_class="span12", id="application_version", label=""), css_class="span6")
#               ,css_class="row-fluid"),
               Field('interpreter',id="application_interpreter"),
               Field('version', id="application_version", label=""),
               'application',
               'git_url',
               'port',
               'before_launch',
               'launch',
               'after_launch',
               'hosts'
               )
