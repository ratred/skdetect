#!/ubr/bin/env bash

find / -name authorized_keys | perl -nae 'chomp; print "$_ "; $a = `cat $_`; while ($a =~ /[^ ]+ ([^\s]+)\n(.*)/){print "$1\n";$a=$2}'
