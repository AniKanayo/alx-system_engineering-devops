# The ULIMIT of the default file is to be improved
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4050/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

# Restart Nginx
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
