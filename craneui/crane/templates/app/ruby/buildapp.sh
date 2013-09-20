#!/bin/bash
cd `dirname "$0"`;
cd {{application_name}};

rbenv rehash;
bundle install

# From here, do what you want to configure your app or anything else
{{before_launch}}

echo '---------------------------------- APP BUILD FINISHED'
