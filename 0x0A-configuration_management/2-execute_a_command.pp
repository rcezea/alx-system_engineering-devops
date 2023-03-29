# execute a command

exec { 'pkill':
  command => '/bin/pkill killmenow',
}
