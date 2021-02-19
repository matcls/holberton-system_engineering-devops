# Fixes Apache 500 error config file typo
file { '/var/www/html/wp-includes/class-wp-locale.phpp':
    ensure => present,
    source => '/var/www/html/wp-includes/class-wp-locale.php',
}
