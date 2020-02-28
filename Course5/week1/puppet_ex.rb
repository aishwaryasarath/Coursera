# puppet resources notes

class sysctl {

	# make sure  the directory exists, some distos don't have it
	file { '/etc/sysctl.d':
	ensure => directory,
	}
}

class timezone {
	file {'/etc/timezone':
	ensure => file,
	content => file,
	replace => true,
	}
}

# puppet class notes

class ntp {
	package { 'ntp':
		ensure => latest,
	}
	file { 'etc/ntp.conf':
		source => 'puppet:///modules/ntp/ntp.conf'
		replace => true,
	}	
	service { 'ntp':
		enable => true,
		ensure => running,
		}
}

# a fact is a variable representing characteristcs of a system
# facts variable is a hash is DSL equivalent to dictionary in python
# package is name of resource
# smartmontools is title of package
# ensure is the attribute and purge is the value
if $facts['is_virtual']{
	package { 'smartmontools':
		ensure => purge,
} else {
	package { 'smartmontools':
		ensure => installed,
}