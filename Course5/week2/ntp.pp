class ntp {
  package { 'ntp':
    ensure => latest,
  }
  file { '/etc/ntp.conf':
    source => '/home/user/ntp.conf',
    replace => true,
    require => Package['ntp'],
    notify => Service['ntp'],
  }
  service {'ntp':
    enable =>true,
    ensure => running,
    require => File['/etc/ntp.conf'],
  }
}

include ntp

# This time, on top of declaring the resources that we need to manage, we're also declaring a few relationships between them. We see that the configuration file requires the NTP package and the service requires the configuration file. This way, Puppet knows that before starting the service, the configuration file needs to be correctly set, and before sending the configuration file, the package needs to be installed. We're also declaring that the NTP service should be notified if the configuration file changes. That way, if we make additional changes to the contents of the configuration file in the future, the service will get reloaded with the new settings. If you look closely, you might notice that the resource types are written in lowercase, but relationships like require or notify use uppercase for the first letter of the resource. This is part of Puppet syntax. We write resource types in lowercase when declaring them, but capitalize them when referring to them from another resource's attributes. This sounds confusing right now, don't worry. It might take a while to wrap your head around it, but it will eventually click. Now, one last thing. At the bottom of the file, we have a call to include NTP. That's why we told Puppet that we want to apply the rules described in a class. For this example, we put the definition of the class and the call to include the class in the same file. Typically, the class is defined in one file and include it in another. We'll checkout examples for this in later videos
