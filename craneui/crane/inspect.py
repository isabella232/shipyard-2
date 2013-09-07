from os import listdir
from data import versions, extensions
from base import crane_path

def list_oses():
    oses_raw = listdir(crane_path('templates/os/'))
    oses_raw.remove('os.tpl')
    oses = []
    for os in oses_raw:
        if os[0] != '.':
           oses.append((os[:-4], os[:-4]))
    return oses

def list_interpreters():
    interpreters_raw = listdir(crane_path('templates/interpreter/'))
    interpreters_raw.remove('interpreter.tpl')
    interpreters = []
    for interpreter in interpreters_raw:
        interpreters.append((interpreter, interpreter))
    return interpreters

def list_versions(interpreter):
    if interpreter not in versions:
       raise Exception("This interpreter is not currently supported.")
    interpreters_versions = []
    for version in versions[interpreter]:
        interpreters_versions.append((version, version))
    return interpreters_versions 

def interpreter_extension(interpreter):
    if interpreter not in extensions:
       raise Exception("This interpreter is not currently supported.")
    return extensions[interpreter]
