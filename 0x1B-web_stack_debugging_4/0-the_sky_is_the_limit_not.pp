# Modifies the maximus of open files allowed for Nginx server.

# Increase only if ULIMIT is set to 15
exec { 'file-limit':
  command => 'sed -i s/15/4096/g /etc/default/nginx',
  path    => ['/usr/local/bin/:/bin/'],
}

# Restart nginx server so it reload config file
exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
