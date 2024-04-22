#!/usr/bin/pup
# Ensure Python and pip are installed
package { 'python3':
  ensure => installed,
}

# Sometimes, 'python3-pip' is the package name for pip3
package { 'python3-pip':
  ensure  => installed,
  require => Package['python3'],  # Ensure Python is installed first
}

# Define a custom fact to ensure that pip3 is the provider
if $facts['os']['family'] == 'Debian' {
  $pip_provider = 'pip3'
} else {
  $pip_provider = 'pip'
}

# Install specific versions of Flask and Werkzeug using pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => $pip_provider,
  require  => Package['python3-pip'],  # Ensure pip3 is installed first
}

package { 'Werkzeug':
  ensure   => '2.1.1',  # Specify the desired version of Werkzeug
  provider => $pip_provider,
  require  => Package['python3-pip'],  # Ensure pip3 is installed first
}

