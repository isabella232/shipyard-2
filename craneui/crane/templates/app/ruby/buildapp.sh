#!/bin/bash
cd `dirname "$0"`;
cd {{application_name}};

# FIXME : what to do with rbenv?
rbenv rehash;
bundle install

# From here, do what you want to configure your app or anything else
{{configuration}}
