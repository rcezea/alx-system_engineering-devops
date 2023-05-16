# fix wordpress apache 500 internal server error

# check if strace is installed
package { 'strace':
  ensure => installed,
}

exec { 'command':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/bin:/usr/sbin:/bin'
}
