# Install Nginx web server (w/ Puppet)
# Requirements:
# Nginx should be listening on port 80
# 4 # Return a page that contains the string "Holberton School" on GET request
# The redirection must be a 301 Moved Permanently
package { 'nginx':
  ensure => installed,
  name   => 'nginx', # Double check
}

file { '/var/www/html/index.html':
  content => 'Holberton School',
}

file_line { 'sites-default':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'root /var/www/html;',
  # Could use a shell command but this is more clean
  line   => '	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
