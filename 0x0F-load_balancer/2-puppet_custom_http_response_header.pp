#Configure custom Nginx HTTP header
exec { '/usr/bin/env apt -y update' : }
-> package { 'nginx':
  ensure => installed,
}
-> file { '/var/www/html/index.html' :
  content => 'Holberton School!',
}
-> file_line { 'add header' :
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By ${hostname};",
  after  => 'server_name _;',
}
-> service { 'nginx':
  ensure => running,
}
