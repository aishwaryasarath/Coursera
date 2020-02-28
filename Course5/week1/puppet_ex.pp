# puppet resources notes
# Infrastructure as code

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
# puppet is a declarative language, we just declare what we want to achieve. The providers 
# are resposible formturning our goals into actions
#python and C are procedural langagues coz we write out the procedure

if $facts['is_virtual']{
	package { 'smartmontools':
		ensure => purge,
} else {
	package { 'smartmontools':
		ensure => installed,
}

# an idempotent action can be performed over and over again without changing the 
# system after the first time the action was performed, and with no unintended side effects
file { '/etc/issue':
	mode => '0644',
	content + "Internal system \l \n",
}

## puppet is stateless, not state is being saved. each puppet run is independent of the other
# exec command is not idempotent though coz exec executes the command for us and that might change the results every time
# ls -l example.txt
# mv example.txt Desktop/

# If the file already exists and has the desired content, then Puppet will understand that no action has to be taken. If the file doesn't exist, then puppet will create it. If the contents or permissions don't match, Puppet will fix them. No matter how many times the agent applies the rule, the end result is that this file will have the requested contents and permissions. Idempotency is a valuable property of any piece of automation. 
# this can be resolved by onlyif
exec { 'move example file':
	command => 'mv /home/user/example.txt /home/user/Desktop',
	onlyif => 'test -e /home/user/example.txt
}


