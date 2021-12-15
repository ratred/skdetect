#!/usr/bin/env bash

sshd -T | egrep -i 'authorizedkeysfile' | perl -lne '@a = split(/\s+/); shift @a; print /([^\/]+)$/ for (@a);'| while read file; do
        echo "find for $file"
        find / -name $file | perl -nae 'chomp; print "$_ "; $a = `cat $_`; while ($a =~ /[^ ]+ ([^\s]+)\n(.*)/){print "$1\n";$a=$2}'
done

