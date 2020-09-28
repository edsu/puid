# puid

This is a very small module that provides a small utility to get the [PRONOM]
Unique Identifier for a file. It's just a small wrapper around the [fido]
library that was created largely for instructional purposes. You will want to
use fido directly if you are wanting to identify files in containers like zip
files or do anything other than get a PUID for a file.

    >>> from puid import get_puid
    >>> get_puid('file.jpg')
    'fmt/42'

[PRONOM]: http://www.nationalarchives.gov.uk/PRONOM/
[fido]: https://github.com/openpreserve/fido
