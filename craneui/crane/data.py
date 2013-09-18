versions =\
{
  'python' : ['2.7.5', '3.3.2'],
  'ruby'   : ['1.9.3-p194', '1.9.3-p392'],
}

extensions =\
{
  'python' : 'py',
  'ruby'   : 'rb',
}

manager =\
{
  'python' : 'source venv/bin/activate',
  'ruby'   : 'rbenv rehash',
}

ports =\
{
  'postgresql' : '5432',
  'redis'      : '6379',
  'mysql'      : '3306',
}

HOST_DATABASE_FOLDER = '/tmp/databases'

volumes =\
{
  'postgresql' : '/var/lib/postgresql'
}
