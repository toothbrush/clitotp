#!/usr/bin/env python

import gnupg
import onetimepass as otp
import os
import pyperclip
import sys

gpg = gnupg.GPG(gnupghome=os.path.expanduser('~/.gnupg'))

my_secret_store_dir = os.path.expanduser('~/.totp')

user_wants = str(sys.argv[1])

secret_file = os.path.join(my_secret_store_dir, user_wants)

print("Will decrypt %s..." % (secret_file))

with open(secret_file, "rb") as f:
    my_secret = gpg.decrypt_file(f)
    my_secret = str(my_secret).strip()

print "Decrypted."

my_token = otp.get_totp(my_secret)

print my_token

pyperclip.copy(my_token)
print "Copied."
