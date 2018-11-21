#!/usr/bin/env python

import gnupg
import onetimepass as otp
import os

gpg = gnupg.GPG(gnupghome=os.path.expanduser('~/.gnupg'))

my_secret_store_dir = os.path.expanduser('~/.totp')

# this would be a parameter / argument
user_wants = 'runbox'

secret_file = os.path.join(my_secret_store_dir, user_wants) + '.gpg'

print("Will decrypt %s..." % (secret_file))

my_secret = gpg.decrypt_file(open(secret_file, "rb"))
my_secret = str(my_secret).strip()

print my_secret

my_token = otp.get_totp(my_secret)

print my_token
