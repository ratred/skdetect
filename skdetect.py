#!/usr/bin/env python
import os

#  Get home dir of every user. Also remove empty values.
with open('/etc/passwd') as r:
    home_dirs = set(filter(None, (l.split(":")[5] for l in r.read().splitlines())))

#  Get authorized_keys file paths in users' home directory
with os.popen("sshd -T 2>/dev/null | egrep -i 'authorizedkeysfile'") as stream:
    authorized_keys_relative_paths = stream.read().split()[1:]

#  Try to find authorized keys in <user_home_directory>/<authorized_keys_relative_path>
for home_dir in home_dirs:
    for authorized_keys_relative_path in authorized_keys_relative_paths:
        try:
            authorized_keys_full_path = os.path.join(home_dir, authorized_keys_relative_path)
            with open(authorized_keys_full_path) as r:
                print("\n".join("%s %s" % (authorized_keys_full_path, l.split()[-1]) for l in r.read().splitlines() if l))
        except IOError:
            pass
