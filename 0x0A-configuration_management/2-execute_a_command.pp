# Execute a Command Using Puppet

exec { 'killmenow':
  command => 'pkill -f ./killmenow',
  path    => '/usr/bin/',
}