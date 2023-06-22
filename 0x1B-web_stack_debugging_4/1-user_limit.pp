# fix for user task

exec { 'holberton user fix:
  command => '/bin/sed -i "s/holberton/# holberton/g" "/etc/security/limits.conf"'
}

