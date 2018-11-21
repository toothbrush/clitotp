#!/usr/bin/env python

import gnupg
from io import StringIO
import os
import sys

gpg = gnupg.GPG(gnupghome=os.path.expanduser('~/.gnupg'))

my_secret_store_dir = os.path.expanduser('~/.totp')

user_wants = str(sys.argv[1])

secret_file = os.path.join(my_secret_store_dir, user_wants + '.gpg')

print("Will insert into: %s" % (secret_file))

my_secret = raw_input("Give me the secret (C-c cancels): ")

recipients = ['0xF2846B1A0D32C442']
encrypted_secret = gpg.encrypt(my_secret, recipients)

with open(secret_file, "wb") as f:
    f.write(str(encrypted_secret))

print "Encrypted and saved."
