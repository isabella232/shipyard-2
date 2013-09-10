#!/bin/sh

# Install rbenv
git clone https://github.com/sstephenson/rbenv.git /usr/local/rbenv
cp /install/rbenv.sh /etc/profile.d/rbenv.sh
chmod +x /etc/profile.d/rbenv.sh

# install ruby-build
mkdir /usr/local/rbenv/plugins && git clone https://github.com/sstephenson/ruby-build.git /usr/local/rbenv/plugins/ruby-build

# install rbenv-gem-rehash
git clone https://github.com/sstephenson/rbenv-gem-rehash.git /usr/local/rbenv/plugins/rbenv-gem-rehash

export RBENV_ROOT="/usr/local/rbenv"
export PATH="$PATH:/usr/local/rbenv/shims:/usr/local/rbenv/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"

# install ruby
rbenv install -v $1 && rbenv rehash && rbenv global $1

# link gem
ln -s /usr/local/rbenv/versions/$1/bin/gem /usr/local/bin/

# install CORE gems
gem update --system && gem install bundler --no-rdoc --no-ri

gem list