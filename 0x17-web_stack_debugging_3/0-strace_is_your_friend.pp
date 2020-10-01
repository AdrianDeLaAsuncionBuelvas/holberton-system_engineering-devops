# Change types in wp settings

exec { 'wp':
  path    => '/bin',
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php"
}
