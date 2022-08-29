# using Puppet to make changes to our configuration file.

file { '/etc/ssh/ssh_config':
  ensure => present,
}
exec { 'SSH client configuration':
  command  => 'echo "  IdentityFile ~/-ssh/school\n  PasswordAuthentication no" >> /etc/ssh/ssh_config',
  path     => [ '/bin', '/sbin' ],
  provider => 'shell',
} 
