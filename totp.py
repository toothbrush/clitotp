#!/usr/bin/env python

import gnupg
import onetimepass as otp
import os
import pyperclip
import sys
import time

gpg = gnupg.GPG(gnupghome=os.path.expanduser('~/.gnupg'))

my_secret_store_dir = os.path.expanduser('~/.totp')

user_wants = str(sys.argv[1])

secret_file = os.path.join(my_secret_store_dir, user_wants)

print("Trying to decrypt %s..." % (secret_file)),

with open(secret_file, "rb") as f:
    my_secret = gpg.decrypt_file(f)
    my_secret = str(my_secret).strip()

print "done."

clock = time.time()
interval_length = 30
intervals_no = int(clock) // interval_length

my_token = otp.get_hotp(my_secret,
                        intervals_no)

print("This token: %06d" % my_token),
pyperclip.copy(my_token)
print("(copied)")

next_token = otp.get_hotp(my_secret,
                          intervals_no+1)

print("Next token: %06d" % next_token)
