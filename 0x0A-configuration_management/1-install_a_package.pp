# Install a Package Using Puppet

package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
}