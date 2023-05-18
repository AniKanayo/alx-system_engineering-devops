# Puppet manifest that changes user limits
exec { 'change_value_to_60':
  command => "/bin/sed -i 's/5/60/g' /etc/security/limits.conf",
}

exec { 'change_value_to_50':
  command => "/bin/sed -i 's/4/50/g' /etc/security/limits.conf",
}
