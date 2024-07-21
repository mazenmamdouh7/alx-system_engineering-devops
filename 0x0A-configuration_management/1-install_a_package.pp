#!/usr/bin/pup
# Puppet manifest to install Flask version 2.1.0 using pip3

# Ensure pip3 is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask version 2.1.0 using pip3
exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
  path    => ['/usr/bin', '/usr/local/bin'],
}