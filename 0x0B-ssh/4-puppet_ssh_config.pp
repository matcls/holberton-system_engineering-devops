# Setup the SSH client configuration file:
# Refuse to authenticate using a password
# Use the private key ~/.ssh/holberton
file_line { 'Set PasswordAuth no':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no',
}

file_line { 'Use IdentityFile':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/holberton',
}
