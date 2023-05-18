# To make holberton user login and open files with no error.

# To improve hard file limit for Holberton user.
exec { 'to-improve-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/60/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# To improve soft file limit for Holberton user.
exec { 'to-improve-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/50/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'

