# Using Puppet to create a manifest that kills a process named killmenow
exec {'Terminated':
command  => 'pkill -f killmenow',
provider => shell,
}
