# Enable the user holberton to login and open files without error.

# Define the file limits for Holberton user.
$hard_limit = 50000
$soft_limit = 50000

# Increase hard file limit for Holberton user.
exec { 'increase-hard-file-limit-for-holberton-user':
  command => "sed -i '/holberton hard/s/5/${hard_limit}/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/',
}

# Increase soft file limit for Holberton user.
exec { 'increase-soft-file-limit-for-holberton-user':
  command => "sed -i '/holberton soft/s/4/${soft_limit}/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/',
}
