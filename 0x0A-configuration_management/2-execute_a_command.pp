# puppet manifest to kill a process named killmenow
exec { 'pkill killmenow':
  command  => 'pkill killmenow',
  provider => shell,
  returns  => [0, 1],
}
