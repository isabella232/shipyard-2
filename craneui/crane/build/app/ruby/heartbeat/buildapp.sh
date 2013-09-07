#!/bin/bash
cd `dirname "$0"`;
cd heartbeat;

# FIXME : what to do with rbenv?
rbenv rehash;
bundle install

# From here, do what you want to configure your app or anything else
